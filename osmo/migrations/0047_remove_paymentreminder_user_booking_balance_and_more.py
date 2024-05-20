# Generated by Django 5.0.4 on 2024-05-18 06:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('osmo', '0046_remove_transaction_next_payment_due_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='paymentreminder',
            name='user',
        ),
        migrations.AddField(
            model_name='booking',
            name='balance',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
        migrations.AddField(
            model_name='paymentreminder',
            name='booking',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='osmo.booking'),
        ),
        migrations.AddField(
            model_name='paymentreminder',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='paymentreminder',
            name='next_payment_date',
            field=models.DateTimeField(),
        ),
    ]
