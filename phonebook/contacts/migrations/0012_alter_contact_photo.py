# Generated by Django 5.0.6 on 2024-08-10 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0011_alter_contact_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='photo',
            field=models.ImageField(upload_to='images'),
        ),
    ]
