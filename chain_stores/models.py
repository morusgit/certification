from django.db import models
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel


class SupplierType(models.Choices):
    ZAVOD = 'Завод'
    IP = 'ИП'
    RC = 'Розничная сеть'


class Supplier(MPTTModel):
    """
    Модель поставщика
    """
    name = models.CharField(unique=True, max_length=200, verbose_name="Наименование", db_index=True)
    type = models.CharField(choices=SupplierType.choices, default=SupplierType.ZAVOD, verbose_name='Тип')
    contacts = models.OneToOneField('Contacts', on_delete=models.CASCADE, verbose_name='Контакты', unique=False)
    email = models.EmailField(blank=True, verbose_name="E-mail")
    products = models.ManyToManyField('Product', verbose_name='Товар', db_index=True)
    arrears = models.FloatField(null=True, blank=True, verbose_name="Задолженность перед поставщиком")
    release_date = models.DateTimeField(auto_now_add=True, verbose_name="Время создания", db_index=True)
    parent = TreeForeignKey('self', on_delete=models.PROTECT, null=True, related_name='children',
                            db_index=True, verbose_name='Поставщик')
    supplier_level = models.IntegerField(blank=True, verbose_name="Уровень")

    def save(self, *args, **kwargs):
        self.supplier_level = self.get_level()
        super(Supplier, self).save(*args, **kwargs)

    def get_level(self, *args, **kwargs):
        if self.type == SupplierType.ZAVOD.value:
            self.supplier_level = 0
        elif self.parent is not None:
            parent = Supplier.objects.get(pk=self.parent.pk)
            if (parent.type == SupplierType.ZAVOD.value and self.type == SupplierType.RC.value) or (parent.type == SupplierType.ZAVOD.value and self.type == SupplierType.IP.value):
                self.supplier_level = 1
            elif parent.type == SupplierType.RC.value and self.type == SupplierType.IP.value:
                self.supplier_level = 2

        return self.supplier_level

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Поставщик'
        verbose_name_plural = 'Поставщики'

    class MPTTMeta:
        order_insertion_by = ['name']


class Contacts(models.Model):
    country = models.CharField(max_length=200, verbose_name="Страна")
    city = models.CharField(max_length=200, verbose_name="Город")
    street = models.CharField(max_length=200, verbose_name="Улица")
    house = models.CharField(max_length=200, verbose_name="Дом")

    def __str__(self):
        return f"{self.country}, {self.city}, {self.street}. {self.house}"

    class Meta:
        verbose_name = 'Контакты'
        verbose_name_plural = 'Контакты'


class Product(models.Model):
    name = models.CharField(unique=True, max_length=200, verbose_name="Наименование", db_index=True)
    model = models.CharField(unique=True, max_length=200, verbose_name="Модель", db_index=True)
    release_date = models.DateField(auto_now_add=True, verbose_name="Дата выхода продукта", db_index=True)

    def __str__(self):
        return f"{self.name} {self.model}"

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
