from django import forms
from django.contrib.auth.models import User
from gcn.models import Club, Night, NightAdmin, UserForm,UserProfileForm,UserPictureForm


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())


    class Meta:
        model = User
        fields = ('username', 'email', 'password')





class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfileForm
        fields = ('website','picture')


class UserPictureForm(forms.ModelForm):
    class Meta:
        model = UserPictureForm
        fields = ('picture',)

