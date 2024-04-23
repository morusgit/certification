from rest_framework import serializers
from users.models import User


class UserSerializers(serializers.ModelSerializer):
    """
    Сериализатор для представления пользователя
    """

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'phone', 'city']
