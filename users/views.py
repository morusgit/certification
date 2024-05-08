from rest_framework import generics
from users.models import User
from users.serializers import UserSerializers


class UserListView(generics.ListAPIView):
    """
    Представление для просмотра списка пользователей
    """
    queryset = User.objects.all()
    serializer_class = UserSerializers


class UserCreateView(generics.CreateAPIView):
    """
    Представление для создания пользователя
    """
    queryset = User.objects.all()
    serializer_class = UserSerializers


class UserRetrieveView(generics.RetrieveAPIView):
    """
    Представление для просмотра пользователя
    """
    queryset = User.objects.all()
    serializer_class = UserSerializers


class UserUpdateView(generics.UpdateAPIView):
    """
    Представление для изменения пользователя
    """
    queryset = User.objects.all()
    serializer_class = UserSerializers


class UserDestroyView(generics.DestroyAPIView):
    """
    Представление для удаления пользователя
    """
    queryset = User.objects.all()
    serializer_class = UserSerializers
