from django.contrib import admin
from app import models


class SingleObjectAddPermissionMixin:
    def has_add_permission(self, *args, **kwargs):
        has_add_permission = super().has_add_permission(*args, **kwargs)
        if self.model.objects.count():
            return False
        return has_add_permission

class ProfileAdmin(SingleObjectAddPermissionMixin, admin.ModelAdmin):
    list_display = ("user", "dob", "age", "phone", "email")

class SocialLinkAdmin(admin.ModelAdmin):
    list_display = ("name", "url")

class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'profile')

class MessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'subject', 'body')

model_admins = [
    (models.SkillModel, SkillAdmin),
    (models.ProfileModel, ProfileAdmin),
    (models.SocialLinkModel, SocialLinkAdmin),
    (models.MessageModel, MessageAdmin),
]

[admin.site.register(*md) for md in model_admins]