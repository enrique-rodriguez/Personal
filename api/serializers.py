from rest_framework.serializers import ModelSerializer
from app import models


class MessageModelSerializer(ModelSerializer):
    class Meta:
        model = models.MessageModel
        fields = "__all__"