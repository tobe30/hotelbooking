from django.urls import path
from core import views 

urlpatterns = [
    path('', views.index, name="index"),
    path('room', views.room, name="room"),
    path('amenities', views.amenite, name="amenities"),
    path('search', views.search, name="search"),
   path('booking/<str:category>/', views.booking, name='booking'),
   


]