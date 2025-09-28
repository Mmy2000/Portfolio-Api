from django.db import models

# Create your models here.


class Contact(models.Model):
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    email = models.EmailField()
    subject = models.CharField(max_length=250)
    message = models.TextField(max_length=3000)

    def __str__(self):
        return self.email
