from django.conf import settings
from drivers import send_message
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from app.models import SettingsModel
from api.utils.captcha import is_valid_captcha
from core.exceptions import InvalidMessageError
from django.utils.translation import ugettext as _
from api.serializers import modelserializer_factory
from app import settings


class MessageListView(APIView):
    serializer_class = modelserializer_factory('app.MessageModel')
    error_messages = {
        'captcha': _("Captcha challenge failed"),
        InvalidMessageError.EMPTY_NAME: _("Sender name must not be empty."),
        InvalidMessageError.EMPTY_BODY: _("Message body must not be empty."),
        InvalidMessageError.ADDRESS: _("The address '%(address)s' is invalid'."),
        InvalidMessageError.EMPTY_SUBJECT: _("Message subject must not be empty."),
        InvalidMessageError.SHORT: _("Message body must be at least %(min_length)s characters long."),
    }
    
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if not is_valid_captcha(request.data.get('recaptcha-response')):
            self.handle_invalid_captcha()
        elif serializer.is_valid(raise_exception=True):
            self.send_message(serializer.data)
        return Response(data=self.data, status=self.status)

    def handle_invalid_captcha(self):
        self.data = {"error": 'captcha', "detail": self.error_messages['captcha']}
        self.status = status.HTTP_400_BAD_REQUEST
    
    def send_message(self, data):
        try:
            self.data = send_message(data, send_limit=settings.get('send_message_limit'))
        except InvalidMessageError as error:
            self.handle_invalid_message(error)
        else:
            self.status = status.HTTP_201_CREATED
    
    def handle_invalid_message(self, error):
        self.data = {"error": error.reason, "detail": self.error_messages[error.reason] % error.kwargs}
        self.status = status.HTTP_400_BAD_REQUEST

list = MessageListView.as_view()