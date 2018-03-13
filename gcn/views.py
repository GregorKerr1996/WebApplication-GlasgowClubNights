from django.shortcuts import render
from django.http import HttpResponse
from gcn.forms import UserForm, UserProfileForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required


# Create your views here.




def home(request):
    return render(request, 'glasgowclubnights/home.html')


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


def reviews(request):
    return render(request, 'glasgowclubnights/reviews.html')


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
