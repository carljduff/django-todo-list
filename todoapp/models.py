from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Todo(models.Model):
    label = models.CharField(max_length=500)
    description = models.CharField(max_length=1000)
    category = models.ForeignKey("Category", on_delete=models.CASCADE)
    PRIORITY_CHOICES = [
        ('LOW', 'Low'),
        ('MEDIUM', 'Medium'),
        ('URGENT', 'Urgent')
    ]
    priority = models.CharField(max_length = 6, choices = PRIORITY_CHOICES, default = 'LOW')
    due_date = models.DateField(blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.label

class Category(models.Model):
    label = models.CharField(max_length=250)
    COLOR_CHOICES = [
        ('BLUE', 'Blue'),
        ('RED', 'Red'),
        ('GREEN', 'Green'),
        ('PURPLE', 'Purple'),
        ('PINK', 'Pink'),
        ('BLACK', 'Black')
    ]
    color = models.CharField(max_length=20, choices = COLOR_CHOICES, default = 'BLUE')
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.label

    class Meta:
        verbose_name_plural = 'Categories'

class Event(models.Model):
    title = models.CharField(max_length=500)
    description = models.CharField(max_length = 2000)
    date = models.DateField(blank=False, null=False)
    start_time = models.TimeField(auto_now=False, auto_now_add=False)
    end_time = models.TimeField(auto_now=False, auto_now_add=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
