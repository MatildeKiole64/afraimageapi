from django.contrib.auth import authenticate
from rest_framework import serializers, status
from rest_framework import exceptions


class ImageSerializer(serializers.Serializer):
    img = serializers.FileField()
    quality = serializers.IntegerField()
