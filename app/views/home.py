from django.views.generic import TemplateView
from app import models
from django.utils import translation

class HomeView(TemplateView):
    template_name = "app/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["profile"] = models.ProfileModel.fetch()
        context["social_links"] = models.SocialLinkModel.objects.all()
        return context
    
home = HomeView.as_view()