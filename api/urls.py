from api.views import messages
from django.urls import path, include
from api import views


app_name = "api"

messages_urls = ([
    path("", views.messages.list, name="messages")
])


urlpatterns = [
    path("messages/", include(messages_urls))
]