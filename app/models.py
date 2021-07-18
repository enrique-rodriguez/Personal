from django.db import models
from datetime import date, timedelta
from django.utils.translation import ugettext_lazy as _
from django.core.exceptions import ImproperlyConfigured
from django.contrib.auth import get_user_model

UserModel = get_user_model()


def get_default_user():
    return UserModel.objects.first()

def get_default_profile():
    return ProfileModel.objects.first()

class ProfileModel(models.Model):
    class Meta:
        verbose_name = _("Profile")
        verbose_name_plural = _("Profiles")
    user = models.ForeignKey(verbose_name=_("User"), default=get_default_user, to=UserModel, on_delete=models.CASCADE)
    phone = models.CharField(verbose_name=_("Phone Number"), max_length=20)
    email = models.EmailField(verbose_name=_("Email Address"))
    dob = models.DateField(verbose_name=_("Date of Birth"), default=date.today, null=True)
    city = models.CharField(verbose_name=_("City"), default='', max_length=100)
    country = models.CharField(verbose_name=_("Country"), default='', max_length=60)

    @property
    def age(self):
        diff = date.today() - self.dob
        return diff.days//365
    
    @property
    def address(self):
        return f"{self.city}, {self.country}"

    @classmethod
    def fetch(cls):
        if not cls.objects.count():
            raise ImproperlyConfigured("Profile does not exists. Create a Profile in the admin site.")
        return cls.objects.first()

    def __str__(self):
        return self.user.username


class SkillModel(models.Model):
    class Meta:
        verbose_name = _("Skill")
        verbose_name_plural = _("Skills")
    name = models.CharField(verbose_name=_("Skill"), max_length=50)
    profile = models.ForeignKey(verbose_name=_("Profile"), default=get_default_profile, to=ProfileModel, on_delete=models.CASCADE, related_name="skills")

    def __str__(self):
        return self.name


class SocialLinkModel(models.Model):
    url = models.URLField()
    name = models.CharField(max_length=20)
    icon = models.CharField(max_length=100)