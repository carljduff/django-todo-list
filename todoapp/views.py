from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from django.http import HttpResponse
from django.contrib.auth.models import User
from rest_framework import viewsets, permissions
from rest_framework.filters import SearchFilter, OrderingFilter
from .serializers import TodoSerializer, CategorySerializer, EventSerializer, UserSerializer
from .models import *



class TodoViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Todos to be viewed or edited.
    """
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    # permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    # /api/todos?user__first_name= 
    filterset_fields = ('user__first_name',)
    # filterset_fields = ['user_id']

class CategoryViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Categories to be viewed or edited.
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['user_id']
    search_fields = []
    # permission_classes = [permissions.IsAuthenticated]

class EventViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Events to be viewed or edited.
    """
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['user_id']
    # permission_classes = [permissions.IsAuthenticated]

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    # users/?search=
    search_fields = ['=first_name', 'first_name']
    
