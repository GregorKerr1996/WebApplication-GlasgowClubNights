from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User



class Club(models.Model):
    name = models.CharField(max_length=128, unique=True)

    def __str__(self):
        return self.name


class Night(models.Model):
    club_list = models.ForeignKey(Club)
    night_name = models.CharField(max_length=128)
    night_day = models.CharField(max_length=128)
    club_rating = models.IntegerField(null=True)

    def __str__(self):
        return self.night_name


# Create your models here.
class NightAdmin(admin.ModelAdmin):
    list_display = ('night_name', 'club_list')


class userprofile(models.Model):
    user = models.OneToOneField(User)
    website = models.URLField(blank=True)
    picture = models.ImageField(upload_to='profile_images', blank=True)
    def __str__(self):
        return self.user.username
