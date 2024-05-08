from rest_framework import generics
from django_filters import rest_framework as filters
from chain_stores.models import Supplier, Contacts, Product
from chain_stores.serializers import SupplierSerializers, ContactsSerializers, ProductSerializers, \
    SupplierUpdateSerializers


class SupplierCreateView(generics.CreateAPIView):
    """
    Представление для создания поставщика
    """
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializers


class SupplierUpdateView(generics.UpdateAPIView):
    """
    Представление для изменения поставщика
    """
    queryset = Supplier.objects.all()
    serializer_class = SupplierUpdateSerializers


class SupplierListView(generics.ListAPIView):
    """
    Представление для просмотра списка поставщиков
    """
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializers
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = ['contacts__country', 'name']


class SupplierRetrieveView(generics.RetrieveAPIView):
    """
    Представление для просмотра поставщика
    """
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializers


class SupplierDestroyView(generics.DestroyAPIView):
    """
    Представление для удаления поставщика
    """
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializers


class ContactsCreateView(generics.CreateAPIView):
    """
    Представление для создания контактов
    """
    queryset = Contacts.objects.all()
    serializer_class = ContactsSerializers


class ContactsListView(generics.ListAPIView):
    """
    Представление для просмотра списка контактов
    """
    queryset = Contacts.objects.all()
    serializer_class = ContactsSerializers


class ContactsUpdateView(generics.UpdateAPIView):
    """
    Представление для изменения контактов
    """
    queryset = Contacts.objects.all()
    serializer_class = ContactsSerializers


class ProductCreateView(generics.CreateAPIView):
    """
    Представление для создания продукта
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializers


class ProductListView(generics.ListAPIView):
    """
    Представление для просмотра списка продуктов
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializers


class ProductUpdateView(generics.UpdateAPIView):
    """
    Представление для изменения продукта
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializers