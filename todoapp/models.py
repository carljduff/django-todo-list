from django.db import models

# Create your models here.
class Todo(models.Model):
    label = models.CharField(max_length=500)
    description = models.CharField(max_length=1000)
    category = models.ForeignKey(Users, on_delete=models.CASCADE)
    LOW = 'LOW'
    MEDIUM = 'MEDIUM'
    URGENT = 'URGENT'
    PRIORITY_CHOICES = [
        (LOW, 'Low'),
        (MEDIUM, 'Medium'),
        (URGENT, 'Urgent')
    ]
    priority = models.Charfield(max_length = 6, choices = PRIORITY_CHOICES, default = LOW)

class Category(models.Model):
    label = models.CharField(max_length=250)
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE)