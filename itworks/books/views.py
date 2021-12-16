from django.shortcuts import render
from django.http import HttpResponse


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
