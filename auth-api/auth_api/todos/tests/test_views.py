from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIRequestFactory, force_authenticate

from users.models import User
from users.serializers import UserSerializer
from todos.views import TodoList, TodoDetail
from todos.models import Todo
from todos.serializers import TodoSerializer


class TestTodos(TestCase):

    def setUp(self):
        self.request_factory = APIRequestFactory()
        self.user = User(username='testuser1')
        self.user.set_password('12345')
        self.user.save()

    def test_get_all_todos(self):
        todo1 = Todo(name='todo1', user=self.user)
        todo1.save()
        todo2 = Todo(name='todo2', user=self.user)
        todo2.save()

        request = self.request_factory.get(reverse('todos:todo-list'), format='json')
        force_authenticate(request, user=self.user)
        view = TodoList.as_view()
        response = view(request)
        response.render()
        todos = Todo.objects.all()
        serializer = TodoSerializer(todos, many=True, context={'request': request})

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_get_single_todo(self):
        todo1 = Todo(name='todo1', user=self.user)
        todo1.save()
        todo2 = Todo(name='todo2', user=self.user)
        todo2.save()

        request = self.request_factory.get(reverse('todos:todo-detail', kwargs={'pk': 2}), format='json')
        force_authenticate(request, user=self.user)
        view = TodoDetail.as_view()
        response = view(request, pk=2)
        response.render()
        todo = Todo.objects.get(pk=2)
        serializer = TodoSerializer(todo, context={'request': request})

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_get_invalid_single_todo(self):
        todo1 = Todo(name='todo1', user=self.user)
        todo1.save()
        todo2 = Todo(name='todo2', user=self.user)
        todo2.save()

        request = self.request_factory.get(reverse('todos:todo-detail', kwargs={'pk': 3}), format='json')
        force_authenticate(request, user=self.user)
        view = TodoDetail.as_view()
        response = view(request, pk=3)
        response.render()
        todo = Todo.objects.get(pk=2)

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_post_todo(self):
        post_data = {
            'name': 'todo1',
        }
        request = self.request_factory.post(reverse('todos:todo-list'), post_data, format='json')
        force_authenticate(request, user=self.user)
        view = TodoList.as_view()
        response = view(request)
        response.render()

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Todo.objects.all().count(), 1)

    def test_post_todo_with_invalid_data(self):
        post_data = {
            'improper_property': 'todo1',
        }
        request = self.request_factory.post(reverse('todos:todo-list'), post_data, format='json')
        force_authenticate(request, user=self.user)
        view = TodoList.as_view()
        response = view(request)
        response.render()

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_update_todo(self):
        todo1 = Todo(name='todo1', user=self.user)
        todo1.save()
        update_data = {
            'name': 'updatedName',
        }
        self.assertEqual(Todo.objects.get(pk=1).name, 'todo1')

        request = self.request_factory.patch(reverse('todos:todo-detail', kwargs={'pk': 1}), update_data, format='json')
        force_authenticate(request, user=self.user)
        view = TodoDetail.as_view()
        response = view(request, pk=1)
        response.render()

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Todo.objects.get(pk=1).name, 'updatedName')

    def test_invalid_todo(self):
        todo1 = Todo(name='todo1', user=self.user)
        todo1.save()
        update_data = {
            'name': 'updatedName',
        }
        self.assertEqual(Todo.objects.get(pk=1).name, 'todo1')

        request = self.request_factory.patch(reverse('todos:todo-detail', kwargs={'pk': 2}), update_data, format='json')
        force_authenticate(request, user=self.user)
        view = TodoDetail.as_view()
        response = view(request, pk=2)
        response.render()

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(Todo.objects.get(pk=1).name, 'todo1')

    def test_delete_todo(self):
        todo1 = Todo(name='todo1', user=self.user)
        todo1.save()
        self.assertTrue(Todo.objects.all().count() == 1)

        request = self.request_factory.delete(reverse('todos:todo-detail', kwargs={'pk': 1}), format='json')
        force_authenticate(request, user=self.user)
        view = TodoDetail.as_view()
        response = view(request, pk=1)
        response.render()

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertTrue(Todo.objects.all().count() == 0)

    def test_delete_invalid_todo(self):
        todo1 = Todo(name='todo1', user=self.user)
        todo1.save()
        self.assertTrue(Todo.objects.all().count() == 1)

        request = self.request_factory.delete(reverse('todos:todo-detail', kwargs={'pk': 2}), format='json')
        force_authenticate(request, user=self.user)
        view = TodoDetail.as_view()
        response = view(request, pk=2)
        response.render()

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertTrue(Todo.objects.all().count() == 1)
