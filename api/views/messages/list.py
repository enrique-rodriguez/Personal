from drivers import send_message
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import JSONParser


class MessageListView(APIView):
    
    def post(self, request):
        """
        data = JSONParser().parse(request)
        serializer = self.serializer_class(data)
        if serializer.is_valid():
            self.send_message(serializer.data)
        return Response(data=self.data, status=self.status)
        """

        self.send_message({})
        data = JSONParser().parse(request)
        return Response(data=data, status=status.HTTP_201_CREATED)
    
    def send_message(self, data):
        try:
            send_message(data)
        except:
            pass

list = MessageListView.as_view()