# Generated by Django 5.0.4 on 2024-05-01 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('osmo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plan',
            name='img',
            field=models.ImageField(null=True, upload_to='images/'),
        ),
    ]
