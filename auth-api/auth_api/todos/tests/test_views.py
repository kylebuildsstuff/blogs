from rest_framework import status
from rest_framework.test import APIRequestFactory, force_authenticate

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
        pass

    def test_get_single_todo(self):
        pass

    def test_get_invalid_single_todo(self):
        pass

    def test_post_todo(self):
        pass

    def test_post_todo_with_invalid_data(self):
        pass

    def test_update_todo(self):
        pass

    def test_invalid_todo(self):
        pass

    def test_delete_todo(self):
        pass

    def test_delete_invalid_todo(self):
        pass
