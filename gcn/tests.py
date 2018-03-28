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

    def test_home_using_template(self):
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

        
    def test_login_provides_error_message(self):
        # Access login page
        try:
            response = self.client.post(reverse('login'), {'username': 'wronguser', 'password': 'wrongpass'})
        except:
            try:
                response = self.client.post(reverse('gcn:login'), {'username': 'wronguser', 'password': 'wrongpass'})
            except:
                return False

        print(response.content.decode('ascii'))
        try:
            self.assertIn('wronguser', response.content.decode('ascii'))
        except:
            self.assertIn('Invalid login details supplied.', response.content.decode('ascii'))

    def test_login_form_is_displayed_correctly(self):
        # Access login page
        try:
            response = self.client.get(reverse('login'))
        except:
            try:
                response = self.client.get(reverse('gcn:login'))
            except:
                return False

        # Check form display
        # Header
        self.assertIn('login', response.content.decode('ascii'))

        # Username label and input text
        self.assertIn('Username', response.content.decode('ascii'))
        self.assertIn('input type="text"', response.content.decode('ascii'))
        self.assertIn('name="username"', response.content.decode('ascii'))

        # Password label and input text
        self.assertIn('Password', response.content.decode('ascii'))
        self.assertIn('input type="password"', response.content.decode('ascii'))
        self.assertIn('name="password"', response.content.decode('ascii'))

        # Submit button
        self.assertIn('Sign in', response.content.decode('ascii'))
        self.assertIn('value="Submit"', response.content.decode('ascii'))

    def test_login_redirects_to_home(self):
        # Create a user
        # create_user()  # Access login page via POST with user data
        try:
            response = self.client.post(reverse('login'), {'username': 'testuser', 'password': 'Hello123'})
        except:
            try:
                response = self.client.post(reverse('gcn:login'), {'username': 'testuser', 'password': 'Hello123'})
            except:
                return False

        # Check it redirects to index
        self.assertEquals(response.status_code, 200)

    def create_user(self):
        # Create a user
        from gcn.models import UserForm

        user = UserForm.user("testuser")
        password = UserForm.password("Hello123")
        user.set_password(password)
        user.save()

        # Create a user profile

        return user