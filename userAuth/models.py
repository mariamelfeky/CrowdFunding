from django.db import models
from django.core.validators import RegexValidator


class UserPhone (models.Model):
    phone_regex = RegexValidator(regex=r'^[+-]?[0-9]+$')
    user_phone = models.CharField(validators=[phone_regex], max_length=11)




class User (models.Model):
    user_fname = models.CharField(max_length=10)
    user_lname = models.CharField(max_length=10)
    user_picture = models.ImageField(upload_to="user_images/")
    user_password = models.CharField(max_length=50)
    phone_id = models.ForeignKey(UserPhone, on_delete=models.CASCADE)

