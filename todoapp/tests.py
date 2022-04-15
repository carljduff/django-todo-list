# from django.test import TestCase, Client
# import json
# from rest_framework import status
# from django.urls import reverse
# from .models import Todo
# from .serializers import TodoSerializer

# client = Client()

# Create your tests here.

# class TestListCreateTodos(TestCase):
#     def test_create_todos(self):
#         test_todo={'label': 'Test', 'description': 'TEST', 'category': '3', 'priority': 'LOW', 'user': '1'}
#         response = self.client.post(reverse("todos"), test_todo)
#         self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
