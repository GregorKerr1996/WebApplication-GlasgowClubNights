from django.db import models

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
