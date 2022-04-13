from django.contrib import admin
from .models import Todo, Category, Event

admin.site.register(Todo)
admin.site.register(Category)
admin.site.register(Event)
# Register your models here.
