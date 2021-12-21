from django.urls import path

import profiles.views
from profiles.views import CreateProfileView

urlpatterns = [
    path("newprofile", CreateProfileView.as_view(), name ="createprofile")
]
