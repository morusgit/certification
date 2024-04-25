from django.contrib import admin
from django.utils.html import format_html
from chain_stores.models import Supplier, Contacts, Product


@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    fields = ['name', 'contacts', 'products', 'provider', 'arrears']
    list_display = ['name', 'contacts', 'provider', 'get_provider', 'arrears', 'release_date', 'get_products']
    list_display_links = ['name', 'get_provider']
    list_filter = ['contacts__city']
    filter_horizontal = ['products']
    actions = ['set_arrears']

    @admin.display(description="Товары")
    def get_products(self, instance):
        return [product.name for product in instance.products.all()]

    @admin.display(description="Ссылка на поставщика")
    def get_provider(self, obj):
        return format_html("<a href='{url}'>{url}</a>", url=obj.provider_id)

    @admin.action(description="Удалить заделженность перед поставщиком")
    def set_arrears(self, request, queryset):
        count = queryset.update(arrears=0)
        self.message_user(request, f"Изменено {count} записей!")


@admin.register(Contacts)
class ContactsAdmin(admin.ModelAdmin):
    fields = ['email', 'country', 'city', 'street', 'house']
    list_display = ['email', 'country', 'city', 'street', 'house']
    list_filter = ['country', 'city', 'street', 'house']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    fields = ['name', 'model']
    list_display = ['name', 'model', 'release_date']
    list_filter = ['name', 'model', 'release_date']
