import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','glasgow_club_nights.settings')

import django
django.setup()
from gcn.models import Club, Night

def populate():
    kushion = [
        {"night_name": "Juicy Tuesday", "night_day": "Tuesday", "club_rating": "5" },
        {"night_name": "Loco Thursday", "night_day": "Thursday", "club_rating": "2" },
        {"night_name": "Milk Friday", "night_day": "Friday", "club_rating": "3"},
        {"night_name": "Kushion Saturday", "night_day": "Saturday", "club_rating": "3"}
    ]

    shimmy = [
        {"night_name": "No Way Wednesday", "night_day": "Wednesday", "club_rating": "5"},
        {"night_name": "Paper Friday", "night_day": "Friday", "club_rating": "2"},
        {"night_name": "Shimmy Saturday", "night_day": "Saturday", "club_rating": "3"},
        {"night_name": "Likewise Sunday", "night_day": "Sunday", "club_rating": "3"},
    ]

    bamboo = [
        {"night_name": "WNB Wednesday", "night_day": "Wednesday", "club_rating": "5"},
        {"night_name": "Get Loose Fridays", "night_day": "Friday", "club_rating": "2"},
        {"night_name": "Bamboo Saturdays", "night_day": "Saturday", "club_rating": "3"},
        {"night_name": "Disco Badger Sundays", "night_day": "Sunday", "club_rating": "3"},
    ]

    clubs = {"Kushion": {"club_nights": kushion},
             "Shimmy":{"club_nights":shimmy},
             "Bamboo": {"club_nights":bamboo}}

    for club, clubs_data in clubs.items():
        c=add_club(club)
        for p in clubs_data["club_nights"]:
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