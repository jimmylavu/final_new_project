# Generated by Django 5.0.4 on 2024-05-20 11:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('osmo', '0067_remove_booking_reminder_paymentreminder_booking'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='paymentreminder',
            name='booking',
        ),
        migrations.AddField(
            model_name='booking',
            name='reminder',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='osmo.paymentreminder'),
        ),
    ]
