import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','glasgow_club_nights.settings')

import django
django.setup()
from gcn.models import Club, Night

def populate():
    kushion = [
        {"night_name": "Juicy Tuesdays", "night_day": "Tuesday", "club_rating": "5" },
        {"night_name": "Loco Thursdays", "night_day": "Thursday", "club_rating": "2" },
        {"night_name": "Milk Fridays", "night_day": "Friday", "club_rating": "3"}
    ]

    clubs = {"Clubs": {"Club Name": kushion}}

    for club, clubs_data in clubs.items():
        c=add_club(club)
        for p in clubs_data["Club Name"]:
            add_night(c, p["night_name"], p["night_day"], p["club_rating"])

def add_night(club, night_name, night_day, club_rating):
    p = Night.objects.get_or_create(club_list=club, night_name = night_name, night_day = night_day)[0]
    p.club_rating = club_rating
    p.save()
    return p

def add_club(name):
    c = Club.objects.get_or_create(name=name)[0]
    c.save()
    return c

if __name__ =='__main__':
    print("Starting Rango population script...")
    populate()