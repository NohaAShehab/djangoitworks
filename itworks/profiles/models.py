from django.db import models


# Create your models here.

class ProfileModel(models.Model):
    user_img = models.FileField(upload_to="profiles/static/profiles/images")
    name = models.CharField(max_length=100, default="test")
    age = models.IntegerField(default=10)
