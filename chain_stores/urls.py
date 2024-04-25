from django.urls import path

from chain_stores.views import SupplierCreateView, SupplierListView, SupplierUpdateView, SupplierRetrieveView, \
    SupplierDestroyView, ContactsCreateView, ContactsListView, ContactsUpdateView, ProductListView, ProductCreateView, \
    ProductUpdateView

urlpatterns = [
    path('', SupplierListView.as_view(), name='list'),
    path('create/', SupplierCreateView.as_view(), name='create'),
    path('update/<int:pk>/', SupplierUpdateView.as_view(), name='update'),
    path('retrieve/<int:pk>/', SupplierRetrieveView.as_view(), name='retrieve'),
    path('delete/<int:pk>/', SupplierDestroyView.as_view(), name='delete'),

    path('contacts/list/', ContactsListView.as_view(), name='contacts_list'),
    path('contacts/create/', ContactsCreateView.as_view(), name='contacts_create'),
    path('contacts/update/<int:pk>/', ContactsUpdateView.as_view(), name='contacts_update'),

    path('product/list/', ProductListView.as_view(), name='product_list'),
    path('product/create/', ProductCreateView.as_view(), name='product_create'),
    path('product/update/<int:pk>/', ProductUpdateView.as_view(), name='product_update'),
    ]