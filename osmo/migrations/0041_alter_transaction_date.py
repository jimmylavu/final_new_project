# Generated by Django 5.0.4 on 2024-05-17 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('osmo', '0040_transaction_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='date',
            field=models.DateTimeField(null=True),
        ),
    ]