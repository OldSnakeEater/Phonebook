from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='images')
    subdivision = models.CharField(max_length=255)
    jobtitle = models.CharField(max_length=255)
    number = models.CharField(max_length=255)
    mail = models.EmailField(max_length=255)

    def __str__(self):
        return f"{self.name} {self.subdivision} {self.jobtitle} {self.number} {self.mail} {self.photo}"
# Create your models here.
