from django.test import TestCase
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.core.urlresolvers import reverse
import os
import os.path
from django.template import loader
from django.conf import settings

# Test 6
from django.template import loader
from django.conf import settings

import os.path

# Chapter 4
from django.contrib.staticfiles import finders

# Chapter 9
from gcn.models import UserForm, UserProfileForm, UserPictureForm, Club
from gcn.forms import UserForm, UserProfileForm, UserPictureForm
from django.core.files.uploadedfile import SimpleUploadedFile
from django.core.files.storage import default_storage


class gcnTest(TestCase):
    def test_home_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_index_using_template(self):
        response = self.client.get(reverse('home'))
        self.assertTemplateUsed(response, 'glasgowclubnights/home.html')

    def test_clubList_using_homeBase(self):
        self.client.get(reverse('home'))
        response = self.client.get(reverse('club_list'))
        self.assertTemplateUsed(response, 'glasgowclubnights/club_list.html')

    def test_home_contains_link_to_club_list(self):
        # Access index
        try:
            response = self.client.get(reverse('home'))
        except:
            try:
                response = self.client.get(reverse('club_list'))
            except:
                return False

        # Check if there is text and a link to add category
        self.assertIn('href="' + reverse('club_list') + '"', response.content.decode('ascii'))

    def test_base_template_exists(self):
        # Check base.html exists inside template folder
        path_to_base = settings.TEMPLATE_DIR + '/glasgowclubnights/main_base.html'
        print(path_to_base)
        self.assertTrue(os.path.isfile(path_to_base))

    def test_url_reference_in_home_page_when_not_logged_in(self):
        # Create user and log in

        # Access index page
        response = self.client.get(reverse('home'))

        # Check links that appear for logged person only
        self.assertIn(reverse('login'), response.content.decode('ascii'))
        self.assertIn(reverse('club_list'), response.content.decode('ascii'))
        self.assertIn(reverse('about_us'), response.content.decode('ascii'))
        self.assertIn(reverse('contact_us'), response.content.decode('ascii'))

    def test_registration_form_is_displayed_correctly(self):
        # Access registration page
        try:
            response = self.client.get(reverse('register'))
        except:
            try:
                response = self.client.get(reverse('register'))
            except:
                return False

        # Check form in response context is instance of UserForm
        self.assertTrue(isinstance(response.context['user_form'], UserForm))

        # Check form in response context is instance of UserProfileForm
        self.assertTrue(isinstance(response.context['profile_form'], UserProfileForm))

        user_form = UserForm()
        profile_form = UserProfileForm()

        # Check form is displayed correctly
        self.assertEquals(response.context['user_form'].as_p(), user_form.as_p())
        self.assertEquals(response.context['profile_form'].as_p(), profile_form.as_p())

        # Check submit button
        self.assertIn('type="submit"', response.content.decode('ascii'))

    def test_home_picture_displayed(self):
        response = self.client.get(reverse('glasgow_club_nights:club_list/kushion'))

        # Check if is there an image in index page
        self.assertIn('img src="{{ MEDIA_URL}}kushion.jpg"'.lower(), response.content.decode('ascii').lower())


def create_user():
    # Create a user
    from gcn.models import UserForm

    user = UserForm.user("testuser")
    password = UserForm.password("Hello123")
    user.save()

    # Create a user profile

    return user