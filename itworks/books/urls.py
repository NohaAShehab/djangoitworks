from django.urls import path
from books.views import testfunction, hello, queryfun, \
    home, homebase, index, viewbook, deletebook

urlpatterns = [
    ########## books
    path('test', testfunction, name="test"),  ## request -->
    path('hello/<name>', hello, name="hello"),
    path('querystring', queryfun, name="queryfun"),
    path('iti', home, name="homepage"),
    path('contactus', testfunction, name="contact"),
    path("home", homebase),
    path("index", index, name="booksindex"),
    path("<id>", viewbook, name="viewbook"),
    path("delete/<id>", deletebook, name="deletebook"),
]
