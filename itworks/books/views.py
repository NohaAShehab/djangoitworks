from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from books.models import Book
from django.shortcuts import get_object_or_404
from django.urls import reverse



# Create your views here.

# views created using python function
def testfunction(request):
    print("hi the server will respond shortly")
    print(request)
    return HttpResponse("<h1> Welcome to your first application")


def hello(request, name):
    return HttpResponse(f" <h2> <font color='purple'>Good morning {name}"
                        f"</font> </h2>")


def queryfun(request):
    return HttpResponse("query stirng")


def home(request):
    # return HttpResponse("Home page")
    return render(request, "books/index.html")


def homebase(request):
    return render(request, "books/homepage.html")


def index(request):
    # get all books
    books = Book.objects.all().order_by('id')
    # send them to the template
    return render(request, "books/index.html",
                  context={"books":books})


def viewbook(request, id):
    # book = Book.objects.filter(id=id).first()
    # book = Book.objects.get(pk=id)
    ### best practice
    book = get_object_or_404(Book, pk=id)
    return render(request, "books/view.html",context={"book": book})


def deletebook(request, id):
    book = get_object_or_404(Book, pk=id)
    book.delete()
    backtoindex = reverse("booksindex")
    return HttpResponseRedirect(backtoindex)
