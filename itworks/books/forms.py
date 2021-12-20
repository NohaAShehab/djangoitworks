from django import forms
from books.models import Author


class BookForm(forms.Form):
    title = forms.CharField(max_length=100, label="Book title")
    rating = forms.IntegerField(min_value=1, max_value=5)
    author = forms.ModelChoiceField(Author.objects.all())
    is_best_selling = forms.BooleanField(required=False)
