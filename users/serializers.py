from django.contrib.auth.hashers import make_password
from rest_framework import serializers
from users.models import User


class UserSerializers(serializers.ModelSerializer):
    """
    Сериализатор для представления пользователя
    """
    def validate_password(self, value: str) -> str:
        """
        Hash value passed by user.

        :param value: password of a user
        :return: a hashed version of the password
        """
        return make_password(value)

    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'email', 'phone', 'city']
