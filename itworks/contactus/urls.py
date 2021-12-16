from django.urls import path
from contactus.views import contactus
urlpatterns = [
    #### contactus
    path('', contactus, name="contactus"),
]