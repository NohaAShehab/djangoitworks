from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from books.models import Book, Author
from django.shortcuts import get_object_or_404
from django.urls import reverse
from books.forms import BookForm, BookModelForm
from django import views
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView,UpdateView, DeleteView


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
    # render as a function return http response


def index(request):
    # handle get request
    # get all books
    books = Book.objects.all().order_by('id')
    # send them to the template
    return render(request, "books/index.html",
                  context={"books": books})


# class BooklistView(TemplateView):
#     template_name = "books/index.html"
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context["books"] = Book.objects.all().order_by('id')
#         return context

class BooklistView(ListView):
    template_name = "books/index.html"
    model = Book  # object_list = Book.object.all()
    context_object_name = "books"

    ### return queryset
    #
    # def get_queryset(self):
    #     basequery = super().get_queryset()
    #     # data = basequery.order_by("title")
    #     data = basequery.filter(title__contains='t')
    #     return data


############################################################
def viewbook(request, id):
    book = get_object_or_404(Book, pk=id)
    return render(request, "books/view.html", context={"book": book})


class BookDetailView(DetailView):
    template_name = "books/view.html"
    model = Book
    # access the book object in the template using model name in lowercase


def deletebook(request, id):
    book = get_object_or_404(Book, pk=id)
    book.delete()
    backtoindex = reverse("booksindex")
    return HttpResponseRedirect(backtoindex)


def updateorsave(requestparam, optype, bookid=None):
    title = requestparam.POST["title"]
    rating = requestparam.POST["rating"]
    print(type(requestparam.POST))
    is_best_selling = False
    if "is_best_selling" in requestparam.POST.keys():
        is_best_selling = True

    print(is_best_selling)
    author = requestparam.POST["author"]  # id
    authorobj = get_object_or_404(Author, pk=author)
    if optype == "add":
        b = Book()
    else:
        b = get_object_or_404(Book, pk=bookid)
    b.title = title
    b.rating = rating
    b.is_best_selling = is_best_selling
    b.author = authorobj
    b.save()


def saveCleaneddata(data):
    b = Book()
    b.title = data["title"]
    b.rating = data["rating"]
    b.is_best_selling = data["is_best_selling"]
    b.author = data['author']
    b.save()
    # data["country"] --> queryset , [,,,]
    # add ---> accept one object ,,,, iterate --> list of object
    # convert queryset into obj1, obj2, ,,,, , ,,,, ---> sequence unpacking
    # 1- convert queryset into list
    # unpack list using *
    b.publishing_countries.add(*list(data["country"]))


def createbook(request):
    if request.POST:
        form = BookForm(request.POST)
        print(request.POST["country"])
        if form.is_valid():
            print(form.cleaned_data)
            print(f' this are {form.cleaned_data.get("country")}')
            saveCleaneddata(form.cleaned_data)
            # updateorsave(re quest, "add")
            backtoindex = reverse("booksindex")
            return HttpResponseRedirect(backtoindex)

    authors = Author.objects.all()
    # return render(request, "books/create.html", context={"authors": authors})
    form = BookForm()
    return render(request, "books/create.html", context={"form": form, "authors": authors})


def thankyou(request):
    data = request.POST["title"]
    return HttpResponse(data)


def editbook(request, id):
    if request.POST:
        updateorsave(request, "editbook", id)
        backtoindex = reverse("booksindex")
        return HttpResponseRedirect(backtoindex)

    book = get_object_or_404(Book, pk=id)
    authors = Author.objects.all()
    form = BookForm()
    return render(request, "books/edit.html", context={"book": book, "authors": authors, "form": form})


def createbookModelForm(request):
    # BookModelForm
    if request.POST:
        form = BookModelForm(request.POST)
        form.save()
        backtoindex = reverse("booksindex")
        return HttpResponseRedirect(backtoindex)

    form = BookModelForm()
    return render(request, "books/create.html", context={"form": form})


class CreateBookView(CreateView):
    form_class = BookModelForm
    template_name = "books/create.html"
    # if create ---> successfully
    success_url = "index"

class EditBookView(UpdateView):
    model = Book
    form_class = BookModelForm
    template_name = "books/edit.html"

class DeleteBookView(DeleteView):
    model = Book
    success_url = "/books/index"


class BookView(views.View):
    # provides method
    def get(self, request):
        form = BookModelForm()
        return render(request, "books/create.html", context={"form": form})

    def post(self, request):
        form = BookModelForm(request.POST)
        form.save()
        backtoindex = reverse("booksindex")
        return HttpResponseRedirect(backtoindex)




