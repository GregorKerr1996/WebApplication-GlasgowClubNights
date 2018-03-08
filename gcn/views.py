from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def home(request):

    return render(request, 'glasgowclubnights/home.html')

def about_us(request):

    return render(request, 'glasgowclubnights/about_us.html')

def contact_us(request):

    return render(request, 'glasgowclubnights/contact_us.html')

def club_list(request):

    return render(request, 'glasgowclubnights/club_list.html')

def login(request):

    return render(request, 'glasgowclubnights/login.html')

def reviews(request):

    return render(request, 'glasgowclubnights/reviews.html')

def bamboo(request):

    return render(request, 'glasgowclubnights/club_list/bamboo.html')

def cathouse(request):

    return render(request, 'glasgowclubnights/club_list/cathouse.html')

def firewater(request):

    return render(request, 'glasgowclubnights/club_list/firewater.html')

def garage(request):

    return render(request, 'glasgowclubnights/club_list/garage.html')

def hive(request):

    return render(request, 'glasgowclubnights/club_list/hive.html')

def kokomo(request):

    return render(request, 'glasgowclubnights/club_list/kokomo.html')

def kushion(request):

    return render(request, 'glasgowclubnights/club_list/kushion.html')

def la_cheetah(request):

    return render(request, 'glasgowclubnights/club_list/la_cheetah.html')

def mango(request):

    return render(request, 'glasgowclubnights/club_list/mango.html')

def polo(request):

    return render(request, 'glasgowclubnights/club_list/polo.html')

def sanctuary(request):

    return render(request, 'glasgowclubnights/club_list/sanctuary.html')

def shimmy(request):

    return render(request, 'glasgowclubnights/club_list/shimmy.html')

def subclub(request):

    return render(request, 'glasgowclubnights/club_list/subclub.html')

def swg3(request):

    return render(request, 'glasgowclubnights/club_list/swg3.html')

def viper(request):

    return render(request, 'glasgowclubnights/club_list/viper.html')

