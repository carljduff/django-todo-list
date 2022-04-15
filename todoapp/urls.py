from django.urls import path
from .views import *


urlpatterns = [
    path('', TodoViewSet.as_view(), name="todos")
]