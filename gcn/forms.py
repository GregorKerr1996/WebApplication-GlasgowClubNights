from django import forms
from django import template
from django.contrib.auth.models import User, Group
from gcn.models import Club, Night, NightForm

from gcn.models import Club, Night, NightAdmin, UserForm, UserProfileForm, UserPictureForm, UserReviewForm, UserReview, UserReviewAdmin


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfileForm
        fields = ('website', 'picture')


class UserPictureForm(forms.ModelForm):
    class Meta:
        model = UserPictureForm
        fields = ('picture',)



class UserReviewForm(forms.ModelForm):
    name = UserForm
    club_list = UserReview
    club_rating = forms.IntegerField(max_value=5)

    class Meta:
        model = UserReview
        fields=('name','club_list', 'club_rating',)


class NightForm(forms.ModelForm):
    club_list = Club
    night_name = forms.CharField(max_length=128, help_text="Enter the night name.")
    night_day = forms.CharField(max_length=128, help_text="Enter the night day.")

    class Meta:
        model = Night
        fields = ('club_list', 'night_name', 'night_day',)


