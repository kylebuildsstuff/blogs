from todos.models import Todo
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.reverse import reverse

from todos.serializers import TodoSerializer


class TodoList(generics.ListCreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


class TodoDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TodoSerializer

    def get_queryset(self):
        return Todo.objects.all().filter(username=self.request.user)
