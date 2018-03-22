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

    cathouse = [
        {"night_name": "Cliffhanger", "night_day": "Sunday"},
        {"night_name": "Cathouse Saturdays", "night_day": "Saturday"},
        {"night_name": "Cathouse Fridays", "night_day": "Friday"},
        {"night_name": "Unholy Thursdays", "night_day": "Thursday"},
        {"night_name": "Beast Wednesdays", "night_day": "Wednesday"},
    ]

    firewater = [
        {"night_name": "Camden Rocks", "night_day": "Thursday"},
        {"night_name": "Rockaway Tuesdays", "night_day": "Tuesday"},
        {"night_name": "Open Mic Mondays", "night_day": "Monday"},
    ]

    garage = [
        {"night_name": "I Love Garage Saturdays", "night_day": "Saturday"},
        {"night_name": "Fresh Beats Fridays", "night_day": "Friday"},
        {"night_name": "Element Thursday", "night_day": "Thursday"},
        {"night_name": "Wrap-it Wednesday", "night_day": "Wednesday"},
        {"night_name": "Tag Tuesday", "night_day": "Tuesday"},
        {"night_name": "Bare Mondays", "night_day": "Monday"}
    ]
    
    hive = [
        {"night_name": "Switch Saturdays", "night_day": "Saturday"},
        {"night_name": "HIVE Thursday", "night_day": "Thursday"},
      ]

    kokomo = [
        {"night_name": "Kokomo Saturdays", "night_day": "Saturday"},
        {"night_name": "Movin", "night_day": "Friday"},
        {"night_name": "Party Monster", "night_day": "Thursday"},
        {"night_name": "Mile High Monday", "night_day": "Monday"},
   ]

    mango = [
        {"night_name": "Tropicante Saturdays", "night_day": "Saturday"},
        {"night_name": "Ganas #Noromatic Fridays", "night_day": "Friday"},
        {"night_name": "Latin Connection", "night_day": "Thursday"},
        {"night_name": "Salsa Sunday Social", "night_day": "Sunday"},

    ]

    lacheetah = [
        {"night_name": "Sunday at La Cheetah", "night_day": "Sunday"},

    ]

    polo = [
        {"night_name": "Queer Fridays", "night_day": "Friday"},
        {"night_name": "Lollipop Wednesday", "night_day": "Wednesday"},
        {"night_name": "Text me Tuesday", "night_day": "Tuesday"},
        {"night_name": "Backdoor Mondays", "night_day": "Monday"}
    ]

    sanctuary = [
        {"night_name": "Sanctuary Saturdays", "night_day": "Saturday"},
        {"night_name": "Friday Club", "night_day": "Friday"},
        {"night_name": "Dirty Panda", "night_day": "Wednesday"},
        ]

    subclub = [
        {"night_name": "I Am", "night_day": "Tuesday"},
        {"night_name": "Subculture", "night_day": "Saturday"},

    ]

    viper = [
        {"night_name": "FOMO", "night_day": "Friday"},

        {"night_name": "I Love Wednesdays", "night_day": "Wednesday"},

        {"night_name": "Monday Night Heat", "night_day": "Monday"}
    ]




    clubs = {

        "Kushion": {"club_nights": kushion, "club_rating": 2},
        "Shimmy": {"club_nights": shimmy, "club_rating": 5},
        "Bamboo": {"club_nights": bamboo, "club_rating": 5},
        "Viper": {"club_nights":viper, "club_rating":3},
        "Subclub": {"club_nights":subclub, "club_rating":4},
        "Sanctuary": {"club_nights": sanctuary, "club_rating":2},
        "Polo": {"club_nights":polo, "club_rating":1},
        "La Cheetah": {"club_nights":lacheetah, "club_rating":1},
        "Mango": {"club_nights":mango, "club_rating":3},
        "Kokomo": {"club_nights":kokomo, "club_rating":2},
        "HIVE": {"club_nights":hive, "club_rating":5},
        "Firewater": {"club_nights":firewater, "club_rating":0},
        "Garage":{"club_nights":garage, "club_rating":0},
        "Cathouse":{"club_nights":cathouse, "club_rating":0},
        
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
