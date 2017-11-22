from django.shortcuts import render
from rest_framework import viewsets, filters
import django_filters
from .models import User, Entry
from .serializer import UserSerializer, EntrySerializer
# Create your views here.


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class EntryViewSet(viewsets.ModelViewSet):
    queryset = Entry.objects.all()
    serializer_class = EntrySerializer