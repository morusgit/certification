from django.contrib import admin
from django.utils.html import format_html
from chain_stores.models import Supplier, Contacts, Product


@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    fields = ['name', 'type', 'email', 'contacts', 'products', 'arrears', 'parent', 'supplier_level']
    list_display = ['name', 'get_parent', 'supplier_level', 'email', 'contacts', 'arrears', 'release_date', 'get_products']
    list_display_links = ['name']
    list_filter = ['contacts__city']
    filter_horizontal = ['products']
    actions = ['set_arrears']
    readonly_fields = ['supplier_level']

    @admin.display(description="Товары")
    def get_products(self, instance):
        return [product.name for product in instance.products.all()]

    @admin.display(description="Поставщик")
    def get_parent(self, obj):
        if obj.parent is not None:
            return format_html("<a href='{url}'>{name}</a>", url=obj.parent.id, name=obj.parent.name)
        return "-"

    @admin.action(description="Удалить заделженность перед поставщиком")
    def set_arrears(self, request, queryset):
        count = queryset.update(arrears=0)
        self.message_user(request, f"Изменено {count} записей!")


@admin.register(Contacts)
class ContactsAdmin(admin.ModelAdmin):
    fields = ['country', 'city', 'street', 'house']
    list_display = ['country', 'city', 'street', 'house']
    list_filter = ['country', 'city', 'street', 'house']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    fields = ['name', 'model']
    list_display = ['name', 'model', 'release_date']
    list_filter = ['name', 'model', 'release_date']
