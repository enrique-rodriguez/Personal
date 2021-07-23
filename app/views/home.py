from django.views.generic import TemplateView
from django.conf import settings
from app import models
from django.utils import translation

class HomeView(TemplateView):
    template_name = "app/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["profile"] = models.ProfileModel.fetch()
        context["social_links"] = models.SocialLinkModel.objects.all()
        context["captcha_site_key"] = settings.CAPTCHA_SITE_KEY
        return context
    
home = HomeView.as_view()