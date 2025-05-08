from django.db import models
from phonenumber_field.modelfields import PhoneNumberField # type: ignore

class Website(models.Model):
    name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='logos/')
    fabicon = models.ImageField(upload_to='favicons/')
    address = models.TextField()
    phone = PhoneNumberField(blank=True, null=True, unique=True)
    email = models.EmailField(("Email"), unique=True, null=True, blank=True)
    website = models.URLField(("Website"), unique=True, null=True, blank=True)
    facebook = models.URLField(("Facebook"), unique=True, null=True, blank=True)
    youtube = models.URLField(("Youtube"), unique=True, null=True, blank=True)

    def __str__(self):
        return self.name