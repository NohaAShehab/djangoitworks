from django.urls import path
from books.views import testfunction, hello, queryfun, \
    home, homebase, index, viewbook, deletebook,createbook,\
    thankyou,editbook

urlpatterns = [
    ########## books
    path('test', testfunction, name="test"),  ## request -->
    path('hello/<name>', hello, name="hello"),
    path('querystring', queryfun, name="queryfun"),
    path('iti', home, name="homepage"),
    path('contactus', testfunction, name="contact"),
    path("home", homebase),
    path("index", index, name="booksindex"),
    path("<int:id>", viewbook, name="viewbook"),
    path("delete/<id>", deletebook, name="deletebook"),
    path("create", createbook, name="createbook"),
    path("thank-you",thankyou, name="thankyou"),
    path("edit/<id>",editbook, name="editbook")

]
