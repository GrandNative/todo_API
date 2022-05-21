from django.shortcuts import render, HttpResponse
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from . import models
from rest_framework.permissions import IsAuthenticatedOrReadOnly, AllowAny, IsAuthenticated
from django.contrib.auth import get_user_model
from . import serializers


# Create your views here.
def index(request):
    return HttpResponse('new')


class CreateUser(CreateAPIView):
    model = get_user_model()
    permission_classes = [
        AllowAny  # Or anon users can't register
    ]
    serializer_class = serializers.UserSerializer


class UserTasksList(APIView):
    permission_classes = (IsAuthenticated,)

    @staticmethod
    def get_object(request):
        return models.Task.objects.filter(owner=request.user)

    def get(self, request):
        obj = self.get_object(request)
        response = serializers.TaskSerializer(obj, many=True).data
        return Response(response)
