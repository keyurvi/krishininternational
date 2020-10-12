from django.db import models

class ContactUs(models.Model):
    name = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField(max_length=200)
    class Meta:
        db_table = "contact_us"

# Create your models here.
