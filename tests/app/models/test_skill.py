from django.test import TestCase
from django.utils.translation import ugettext_lazy as _
from app.models import SkillModel, ProfileModel, UserModel

class TestSkillModel(TestCase):

    def test_string_representation(self):
        user = UserModel.objects.create_user(username="username", password="password")
        profile = ProfileModel.objects.create(user=user)
        skill = SkillModel.objects.create(name="Skill", profile=profile)

        self.assertEqual(str(skill), "Skill")
    
    def test_verbose_names(self):
        self.assertEqual(SkillModel._meta.verbose_name, _("Skill"))
        self.assertEqual(SkillModel._meta.verbose_name_plural, _("Skills"))
    
    def test_verbose_field_names(self):
        self.assertEqual(SkillModel._meta.get_field("name").verbose_name, _("Skill"))
        self.assertEqual(SkillModel._meta.get_field("profile").verbose_name, _("Profile"))
