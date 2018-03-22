from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http import HttpResponse
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from gcn.models import Club
from gcn.models import Night
from gcn.models import UserReviewForm
from gcn.forms import NightForm
from gcn.models import UserReview

from gcn.forms import UserForm, UserProfileForm


# Create your views here.

def home(request):
    club_rating_list = Club.objects.order_by('-club_rating')[:4]

    context_dict = {'clubs': club_rating_list}

    response = render(request, 'glasgowclubnights/home.html', context=context_dict)

    return response


def about_us(request):
    return render(request, 'glasgowclubnights/about_us.html')


def contact_us(request):
    return render(request, 'glasgowclubnights/contact_us.html')


def club_list(request):
    return render(request, 'glasgowclubnights/club_list.html')


@login_required
def user_logout(request):
    # Since we know the user is logged in, we can now just log them out.
    logout(request)

    # Take the user back to the homepage.
    return HttpResponseRedirect(reverse('home'))


def register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user

            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']
            profile.save()
            registered = True
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()
    return render(request,
                  'glasgowclubnights/register.html',
                  {'user_form': user_form,
                   'profile_form': profile_form,
                   'registered': registered})


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


def test(request):
    form = UserReviewForm()

    if request.method == 'POST':
        form = UserReviewForm(request.POST)

        if form.is_valid():

            club_review = form.save(commit=True)
            club_review.name = name
            club_review.club_rating = club_rating
            club_review.save()

            return home(request)
        else:
            print(forms.errors)

    return render(request, 'glasgowclubnights/test.html', {'user_review_form': form})


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('home'))
            else:
                return HttpResponse("Your club nights account is disabled.")
        else:
            print("Invalid login details: {0}, {1}".format(username, password))
            return HttpResponse("Invalid login details supplied.")
    else:
        return render(request, 'glasgowclubnights/login.html', {})


def reviews(request):
    form = UserReviewForm()

    if request.method == 'POST':
        form = UserReviewForm(request.POST)

        if form.is_valid():

            club_review = form.save(commit=True)


            return home(request)
        else:
            print(forms.errors)

    return render(request, 'glasgowclubnights/reviews.html', {'form': form})


def add_night(request):
    form = NightForm()

    if request.method == 'POST':
        form = NightForm(request.POST)

        if form.is_valid():
            form.save(commit=True)

            return home(request)
        else:
            print(form.errors)

    return render(request, 'glasgowclubnights/add_page.html', {'form': form})
