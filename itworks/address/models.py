from django.db import models

# Create your models here.
class Address(models.Model):
    street =models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    code = models.CharField(max_length=5)

    def __str__(self):
        return f"{self.street}, {self.city}, {self.code}"

