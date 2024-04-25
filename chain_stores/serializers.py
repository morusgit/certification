from rest_framework import serializers
from chain_stores.models import Supplier, Contacts, Product, SupplierType


class SupplierSerializers(serializers.ModelSerializer):
    """
    Сериализатор для представления поставщика
    """
    class Meta:
        model = Supplier
        fields = '__all__'

class ContactsSerializers(serializers.ModelSerializer):
    """
    Сериализатор для представления контактов
    """
    class Meta:
        model = Contacts
        fields = '__all__'

class ProductSerializers(serializers.ModelSerializer):
    """
    Сериализатор для представления продуктов
    """
    class Meta:
        model = Product
        fields = '__all__'