from django.db import models
from django.urls import reverse
from django.core.validators import MinValueValidator, \
    MaxValueValidator, EmailValidator, URLValidator
from django.utils.text import slugify
from address.models import Address


# Create your models here.
class Country(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name}"


class Author(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, null=True)
    # one to one relation between address and the author
    add = models.OneToOneField(Address, on_delete=models.CASCADE, null=True)

    # add must be unique
    def __str__(self):
        return f"{self.firstname} {self.lastname}"


# ## ORM --> create my first table
class Book(models.Model):
    title = models.CharField(max_length=100)
    # You must tell the model that some field should be null
    # add min and max value
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)])
    # handle one to many relationship
    author = models.ForeignKey(Author, default=1,
                               on_delete=models.CASCADE, related_name='authorbooks')
    is_best_selling = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    slug = models.SlugField(default="",
                            null=False, blank=True,
                            db_index=True)
    # #### many to many relationship
    publishing_countries = models.ManyToManyField(Country, null=True)

    def __str__(self):
        return f"{self.title}"

    def get_absolute_url(self):  # return url
        return reverse("viewbook", args=[self.id])

    def get_delete_url(self):
        return reverse("deletebook", args=[self.id])

    def get_edit_url(self):
        return reverse("editbook", args=[self.id])

    # ## slug---> title.split( ).join(-)
    def save(self, *args, **kwargs):
        # # prepare the sulg to be added ,
        self.slug = slugify(self.title)
        super().save(*args, *kwargs)
