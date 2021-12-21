from django import forms
from books.models import Author, Country


class BookForm(forms.Form):
    title = forms.CharField(max_length=100, label="Book title")
    rating = forms.IntegerField(min_value=1, max_value=5)
    author = forms.ModelChoiceField(Author.objects.all())
    is_best_selling = forms.BooleanField(required=False)
    DEMO_CHOICES = (
        ("1", "Naveen"),
        ("2", "Pranav"),
        ("3", "Isha"),
        ("4", "Saloni"),
    )
    # country = forms.MultipleChoiceField(
    #     choices=DEMO_CHOICES,
    #     widget=forms.CheckboxSelectMultiple,
    #
    # )
    country = forms.ModelMultipleChoiceField(Country.objects.all(),
        widget=forms.CheckboxSelectMultiple)

