from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
from core.models import rooms, Amenities, Booking
from core.forms import BookingForm
from django.contrib import messages
from django.conf import settings
from django.template.loader import render_to_string
from django.core.mail import EmailMessage


# Create your views here.

def index(request):
    rum = rooms.objects.filter(available=True).order_by("-id")

    context ={
        "rum":rum
    }

    return render(request, 'index.html', context)

def room(request):

    room = rooms.objects.filter(available=True).order_by("-id")

    context={
        "room":room
    }

    return render(request, 'room.html', context)

def amenite(request):

    ameniti= Amenities.objects.filter(available=True).order_by("-id")

    context = {
        "ameniti":ameniti
    }
    return render(request, 'amenities.html', context)

def search(request):
    adult = request.GET.get('adult', None) 
    # Check if 'adult' parameter is provided
    if adult is not None:
        category = rooms.objects.filter(adult=adult)
        context = {
            "category": category
        }
        return render(request, 'search.html', context)
    else:
        # Handle the case when 'adult' parameter is not provided
        # You might want to redirect the user or show an error message
        return HttpResponse("Missing 'adult' parameter in the request.")

def booking(request, category):
    # Use get_object_or_404 to return a 404 response if no room is found
    room = get_object_or_404(rooms, category__name=category)

    if request.method == 'POST':
        form = Booking(
            category=request.POST['category'],
            firstname=request.POST['firstname'],
            lastname=request.POST['lastname'],
            phone=request.POST['phone'],
            email=request.POST['email'],
            adult=request.POST['adult'],
            children=request.POST['children'],
            checkin=request.POST['checkin'],
            checkout=request.POST['checkout'],
            request=request.POST['request'],
        )
        form.save()
        html_template = 'register_email.html'
        html_message = render_to_string('register_email.html', {'booking': form})
        #html_message = render_to_string(html_template)
        subject = 'welcome to mem'
        email_form = settings.EMAIL_HOST_USER
        recipient_list = [form.email]
        message = EmailMessage(subject, html_message,
                                   email_form, recipient_list)
        message.content_subtype = 'html'
        message.send()
        messages.success(request, "Profile Updated Successfully.")
        
        # Redirect to the 'booking' view for the same category
        return redirect('booking', category=category)

    context = {
        "room": room,
    }

    return render(request, 'book.html', context)