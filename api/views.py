from rest_framework import generics, permissions
from .permissions import IsMessageOwner
from .models import Message, CustomUser
from .serializers import MessageSerializer, UserSerializer
from django.shortcuts import render
import requests

class UserList(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveUpdateAPIView):
    permission_classes = [IsMessageOwner,]
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer

class MessageList(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

class MessageDetail(generics.RetrieveUpdateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

def index(request):
    return render(request, 'index.html')