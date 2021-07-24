from django.db import models
from datetime import date
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone
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
            return None
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


class MessageModel(models.Model):
    class Meta:
        verbose_name = _("Message")
        verbose_name_plural = _("Messages")
    name = models.CharField(verbose_name=_("Name"), blank=True, max_length=50)
    address = models.CharField(verbose_name=_("Email"), blank=True, max_length=254)
    subject = models.CharField(verbose_name=_("Subject"), blank=True, max_length=50)
    body = models.CharField(verbose_name=_("Body"), blank=True, max_length=1000)
    created = models.DateTimeField(verbose_name=_("Created"), default=timezone.now)


class SettingsModel(models.Model):
    send_message_limit = models.IntegerField(verbose_name=_("Daily message limit per email address."), default=3)

    @classmethod
    def get(cls):
        model = cls.objects.first()
        if not model:
            model = cls.objects.create()
        return model