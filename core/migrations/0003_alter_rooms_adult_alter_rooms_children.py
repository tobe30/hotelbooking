# Generated by Django 5.0 on 2023-12-05 23:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_amenities_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rooms',
            name='adult',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='rooms',
            name='children',
            field=models.IntegerField(default=0),
        ),
    ]
