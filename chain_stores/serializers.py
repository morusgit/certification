from rest_framework import serializers
from chain_stores.models import Supplier, Contacts, Product, SupplierType


class SupplierSerializers(serializers.ModelSerializer):
    """
    Сериализатор для представления поставщика
    """
    class Meta:
        model = Supplier
        fields = '__all__'

    # def create(self, validated_data):
    #     if validated_data['type'] == SupplierType.ZAVOD.value:
    #         validated_data['supplier_level'] = 0
    #     elif validated_data['parent'] is not None:
    #         parent = Supplier.objects.get(pk=self.parent.pk)
    #         if (parent.type == SupplierType.ZAVOD.value and validated_data['type'] == SupplierType.RC.value) or (
    #                 parent.type == SupplierType.ZAVOD.value and validated_data['type'] == SupplierType.IP.value):
    #             self.supplier_level = 1
    #         elif parent.type == SupplierType.RC.value and validated_data['type'] == SupplierType.IP.value:
    #             self.supplier_level = 2
    #     elif validated_data['parent'] is None:
    #         validated_data['supplier_level'] = 0
    #         validated_data['parent'] = None
    #         return Supplier.objects.create(**validated_data)
    #     return Supplier.objects.create(**validated_data)


    # def update(self, instance, validated_data):
    #     if validated_data['type'] == SupplierType.ZAVOD.value:
    #         validated_data['supplier_level'] = 0
    #     elif validated_data['parent'] is not None:
    #         parent = Supplier.objects.get(pk=self.parent.pk)
    #         if (parent.type == SupplierType.ZAVOD.value and validated_data['type'] == SupplierType.RC.value) or (
    #                 parent.type == SupplierType.ZAVOD.value and validated_data['type'] == SupplierType.IP.value):
    #             self.supplier_level = 1
    #         elif parent.type == SupplierType.RC.value and validated_data['type'] == SupplierType.IP.value:
    #             self.supplier_level = 2
    #
    #     instance.save()
    #
    #
    #     return instance

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