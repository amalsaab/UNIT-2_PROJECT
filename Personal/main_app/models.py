from django.db import models

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=64)
    email = models.EmailField()
    subject = models.CharField(max_length=1024)
    message = models.TextField()

