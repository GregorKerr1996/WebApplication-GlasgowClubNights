from django.contrib import admin
from django.contrib.auth.models import User
from django.db import models

#creates models for different forms and folders in the database
class Club(models.Model):
    name = models.CharField(max_length=128, unique=True)
    club_rating = models.BigIntegerField(default=0)

    def __str__(self):
        return self.name


class Night(models.Model):
    club_list = models.ForeignKey(Club)
    night_name = models.CharField(max_length=128)
    night_day = models.CharField(max_length=128)

    def __str__(self):
        return self.night_name


class NightForm(models.Model):
    club_list = models.ForeignKey(Club)
    night_name = models.CharField(max_length=128)
    night_day = models.CharField(max_length=128)

    def __str__(self):
        return self.night_name


# Create your models here.
class NightAdmin(admin.ModelAdmin):
    list_display = ('night_name', 'club_list')


class UserReviewAdmin(admin.ModelAdmin):
    list_display = ('name', 'club_list', 'club_rating',)


class UserForm(models.Model):
    user = models.OneToOneField(User)

    def __str__(self):
        return self.user.username


class UserProfileForm(models.Model):
    website = models.URLField(blank=True)
    picture = models.ImageField(upload_to='profile_images', blank=True)


class UserPictureForm(models.Model):
    picture = models.ImageField(upload_to='profile_images', blank=True)


class UserReview(models.Model):
    name = models.ForeignKey(to=User)
    club_list = models.ForeignKey(Club)
    club_rating = models.BigIntegerField(default=0)

    def __unicode__(self):
        return self.name


class UserReviewForm(models.Model):
    name = models.ForeignKey(to=User)
    club_list = models.ForeignKey(Club)
    club_rating = models.BigIntegerField(default=0)

    def __unicode__(self):
        return self.name
