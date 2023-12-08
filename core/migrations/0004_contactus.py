# Generated by Django 5.0 on 2023-12-06 00:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_alter_rooms_adult_alter_rooms_children'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=200)),
                ('lastname', models.CharField(max_length=200)),
                ('phone', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
                ('adult', models.IntegerField(default=0)),
                ('children', models.IntegerField(default=0)),
                ('checkin', models.TextField()),
                ('checkout', models.DateField(auto_now_add=True)),
                ('request', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name': 'Booking',
                'verbose_name_plural': 'Booking',
            },
        ),
    ]
