from rest_framework import generics
from rest_framework.response import Response
from rest_framework.reverse import reverse

from users.models import User
from users.serializers import UserSerializer


class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UserSerializer

    def get_queryset(self):
        # from IPython import embed; embed();
        return User.objects.all().filter(username=self.request.user)
