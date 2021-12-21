from django import forms
from profiles.models import ProfileModel


# class ProfileForm(forms.Form):
#     user_img = forms.FileField()

class ProfileForm(forms.ModelForm):
    class Meta:
        model = ProfileModel
        fields = "__all__"
