# Generated by Django 5.0.4 on 2024-05-09 17:07

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('osmo', '0021_transaction'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transaction',
            name='amount',
        ),
        migrations.AddField(
            model_name='transaction',
            name='payment',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='osmo.payment'),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
