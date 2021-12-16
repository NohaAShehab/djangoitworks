from django.urls import path
from books.views import testfunction, hello, queryfun, home, homebase
urlpatterns = [
    ########## books
    path('test', testfunction, name="test"),  ## request -->
    path('hello/<name>', hello, name="hello"),
    path('querystring', queryfun, name="queryfun"),
    path('iti', home, name="homepage"),
    path('contactus', testfunction, name="contact"),
    path("home", homebase)
]
