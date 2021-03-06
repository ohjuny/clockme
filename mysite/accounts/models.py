from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class TimeSlot(models.Model):
    profile = models.ForeignKey('Profile', on_delete=models.CASCADE)
    datetime = models.CharField(max_length=16)

    def __str__(self):
        return self.datetime

# Extending Django's default User model by having a OneToOneField with User table.
class Profile(models.Model):
    user = models.OneToOneField(User, related_name="profile", on_delete=models.CASCADE)
    phone_number = PhoneNumberField()

    def __str__(self):
        return self.user.username
