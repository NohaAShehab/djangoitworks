from django.shortcuts import render
from django.views import View
from profiles.forms import ProfileForm
from django.http import HttpResponse


# Create your views here.
def filehandler(file):
    # copy local file to the server
    # 1- create file on the server
    with open("temp/myimg.jpg", "wb+") as dest:
        # divide file into parts
        for chunk in file.chunks():
            dest.write(chunk)


class CreateProfileView(View):
    def get(self, request):
        form = ProfileForm()
        return render(request, "profiles/create_profile.html", context={
            "form": form
        })

    def post(self, request):
        form = ProfileForm(request.POST, request.FILES)
        form.save()
        # print(request.FILES)
        # filehandler(request.FILES["user_img"])
        return HttpResponse(request.FILES)
