from drivers import send_message
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from core.exceptions import InvalidMessageError
from django.utils.translation import ugettext as _
from api.serializers import modelserializer_factory


class MessageListView(APIView):
    serializer_class = modelserializer_factory('app.MessageModel')
    error_messages = {
        InvalidMessageError.EMPTY_NAME: _("Sender name must not be empty."),
        InvalidMessageError.EMPTY_BODY: _("Message body must not be empty."),
        InvalidMessageError.ADDRESS: _("The address '%(address)s' is invalid'."),
        InvalidMessageError.EMPTY_SUBJECT: _("Message subject must not be empty."),
        InvalidMessageError.SHORT: _("Message body must be at least %(min_length)s characters long."),
    }
    
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            self.send_message(serializer.data)
        return Response(data=self.data, status=self.status)
    
    def send_message(self, data):
        try:
            self.data = send_message(data)
        except InvalidMessageError as error:
            self.handle_invalid_message(error)
        else:
            self.status = status.HTTP_201_CREATED
    
    def handle_invalid_message(self, error):
        self.data = {"error": error.reason, "detail": self.error_messages[error.reason] % error.kwargs}
        self.status = status.HTTP_400_BAD_REQUEST

list = MessageListView.as_view()