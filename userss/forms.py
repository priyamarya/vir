from django import forms
from .models import UserProfileInfo


class UserProfileInfoForm(forms.ModelForm):

    class Meta:
        model = UserProfileInfo
        fields = ['profile_pic', 'full_name', 'gender']
