from django.db import models
from django.urls import reverse


# Create your models here.

class Author(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.firstname} {self.lastname}"


# ## ORM --> create my first table
class Book(models.Model):
    title = models.CharField(max_length=100)
    # You must tell the model that some field should be null
    rating = models.IntegerField()
    # author = models.CharField(max_length=100, null=True)
    # handle one to many relationship
    author = models.ForeignKey(Author, default=1, on_delete=models.CASCADE)
    is_best_selling = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title}"

    def get_absolute_url(self):  # return url
        return reverse("viewbook", args=[self.id])

    def get_delete_url(self):
        return reverse("deletebook", args=[self.id])
