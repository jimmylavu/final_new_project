# Generated by Django 5.0.4 on 2024-05-04 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('osmo', '0009_payment_plan_id_booking'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='phone',
            field=models.IntegerField(max_length=20),
        ),
    ]
