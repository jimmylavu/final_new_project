# Generated by Django 5.0.4 on 2024-05-07 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('osmo', '0014_remove_plan_mop_booking_mop'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='status',
            field=models.CharField(choices=[('pending', 'Pending'), ('approved', 'Approved'), ('declined', 'Declined')], default='pending', max_length=20),
        ),
    ]
