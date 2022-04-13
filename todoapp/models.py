from django.db import models

# Create your models here.
class Todo(models.Model):
    label = models.CharField(max_length=500)
    description = models.CharField(max_length=1000)
    category = models.ForeignKey(Users, on_delete=models.CASCADE)

class Category(models.Model):
    label = models.CharField(max_length=250)
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE)