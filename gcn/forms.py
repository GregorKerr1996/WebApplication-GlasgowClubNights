from django import forms
from django.contrib.auth.models import User
from gcn.models import Club, Night, NightAdmin, userprofile


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())


    class Meta:
        model = User
        fields = ('username', 'email', 'password')


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = userprofile
        fields = ('website', 'picture')
