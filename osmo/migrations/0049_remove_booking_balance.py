# Generated by Django 5.0.4 on 2024-05-18 10:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('osmo', '0048_alter_paymentreminder_next_payment_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='balance',
        ),
    ]
