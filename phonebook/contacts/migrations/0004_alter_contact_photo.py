# Generated by Django 5.0.6 on 2024-07-30 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0003_alter_contact_mail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='photo',
            field=models.ImageField(upload_to='images'),
        ),
    ]
