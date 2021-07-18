from django.test import TestCase
from app.models import ProfileModel
from datetime import date, timedelta
from django.utils.translation import ugettext as _
from django.core.exceptions import ImproperlyConfigured
from django.contrib.auth import get_user_model

UserModel = get_user_model()


class TestProfileModel(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.user = UserModel.objects.create_user(username="username", password="password")

    def test_raises_improperly_configured_if_no_profile_exists(self):
        with self.assertRaises(ImproperlyConfigured):
            ProfileModel.fetch()
    
    def test_fetch_returns_the_profile(self):
        profile = ProfileModel.objects.create(user=self.user)
        fetched = ProfileModel.fetch()
        self.assertEqual(profile, fetched)
    
    def test_string_representation(self):
        profile = ProfileModel.objects.create(user=self.user)
        self.assertEqual(str(profile), self.user.username)

    def test_verbose_names(self):
        self.assertEqual(ProfileModel._meta.verbose_name, _("Profile"))
        self.assertEqual(ProfileModel._meta.verbose_name_plural, _("Profiles"))
    
    def test_age(self):
        five_years_ago_3_months = date.today() - timedelta(days=365*5 + 30*3)
        profile = ProfileModel.objects.create(user=self.user, dob=five_years_ago_3_months)
        self.assertEqual(profile.age, 5)
    
    def test_address(self):
        profile = ProfileModel.objects.create(user=self.user, city="City", country="Country")
        self.assertEqual(profile.address, "City, Country")
    
    def test_verbose_field_names(self):
        self.assertEqual(ProfileModel._meta.get_field("user").verbose_name, _("User"))
        self.assertEqual(ProfileModel._meta.get_field("phone").verbose_name, _("Phone Number"))
        self.assertEqual(ProfileModel._meta.get_field("email").verbose_name, _("Email Address"))
        self.assertEqual(ProfileModel._meta.get_field("dob").verbose_name, _("Date of Birth"))
        self.assertEqual(ProfileModel._meta.get_field("city").verbose_name, _("City"))
        self.assertEqual(ProfileModel._meta.get_field("country").verbose_name, _("Country"))