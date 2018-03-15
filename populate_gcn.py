import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'glasgow_club_nights.settings')

import django

django.setup()
from gcn.models import Club, Night


def populate():
    kushion = [
        {"night_name": "Juicy Tuesday", "night_day": "Tuesday"},
        {"night_name": "Loco Thursday", "night_day": "Thursday"},
        {"night_name": "Milk Friday", "night_day": "Friday"},
        {"night_name": "Kushion Saturday", "night_day": "Saturday"}
    ]

    shimmy = [
        {"night_name": "No Way Wednesday", "night_day": "Wednesday"},
        {"night_name": "Paper Friday", "night_day": "Friday"},
        {"night_name": "Shimmy Saturday", "night_day": "Saturday"},
        {"night_name": "Likewise Sunday", "night_day": "Sunday"},
    ]

    bamboo = [
        {"night_name": "WNB Wednesday", "night_day": "Wednesday"},
        {"night_name": "Get Loose Fridays", "night_day": "Friday"},
        {"night_name": "Bamboo Saturdays", "night_day": "Saturday"},
        {"night_name": "Disco Badger Sundays", "night_day": "Sunday"}
    ]

    clubs = {

        "Kushion": {"club_nights": kushion, "club_rating": 2},
        "Shimmy": {"club_nights": shimmy, "club_rating": 5},
        "Bamboo": {"club_nights": bamboo, "club_rating": 5}
    }

    for club, club_data in clubs.items():
        c = add_club(club, club_data["club_rating"])
        for p in club_data["club_nights"]:
            add_night(c, p["night_name"], p["night_day"])

def add_night(club, night_name, night_day):
    p = Night.objects.get_or_create(club_list=club, night_name=night_name, night_day=night_day)[0]

    p.save()
    return p


def add_club(name, club_rating):
    c = Club.objects.get_or_create(name=name)[0]
    c.club_rating = club_rating
    c.save()
    return c


if __name__ == '__main__':
    print("Starting Rango population script...")
    populate()
