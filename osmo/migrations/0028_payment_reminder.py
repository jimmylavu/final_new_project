# Generated by Django 5.0.4 on 2024-05-11 18:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('osmo', '0027_remove_payment_total_payable'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='reminder',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='osmo.paymentreminder'),
        ),
    ]