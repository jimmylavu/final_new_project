# Generated by Django 5.0.4 on 2024-05-17 14:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('osmo', '0038_booking_amount'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='amount',
        ),
    ]
