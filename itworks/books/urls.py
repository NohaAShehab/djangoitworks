from django.urls import path

import books.views
from books.views import testfunction, hello, queryfun, \
    home, homebase, index, viewbook, deletebook,createbook,\
    thankyou,editbook,createbookModelForm, BooklistView, BookDetailView, CreateBookView, \
    EditBookView, DeleteBookView

urlpatterns = [
    ########## books
    path('test', testfunction, name="test"),  ## request -->
    path('hello/<name>', hello, name="hello"),
    path('querystring', queryfun, name="queryfun"),
    path('iti', home, name="homepage"),
    path('contactus', testfunction, name="contact"),
    path("home", homebase),
    # path("index", index, name="booksindex"),
    path("index", BooklistView.as_view(), name="booksindex"),
    # path("<int:id>", viewbook, name="viewbook"),
    path("<int:pk>", BookDetailView.as_view(), name="viewbook"),

    # path("delete/<id>", deletebook, name="deletebook"),
    path("delete/<int:pk>", DeleteBookView.as_view(), name="deletebook"),

    path("create", createbook, name="createbook"),
    path("thank-you",thankyou, name="thankyou"),
    # path("edit/<id>",editbook, name="editbook"),
    path("edit/<int:pk>", EditBookView.as_view(), name="editbook"),

    # path("createbookmodel", createbookModelForm, name="createbookmodel"),
    # class based views
    # path("createbookmodel", books.views.BookView.as_view(),
    #      name="createbookmodel"),

    path("createbookmodel", CreateBookView.as_view(),
             name="createbookmodel"),
]
