# Generated by Django 5.0.6 on 2024-08-06 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0005_contact_jobtitle'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='photo',
            field=models.ImageField(upload_to='contacts/static/images'),
        ),
    ]
