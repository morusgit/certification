from django.db import models


class Supplier(models.Model):
    """
    Модель поставщика
    """
    name = models.CharField(unique=True, max_length=200, verbose_name="Наименование", db_index=True)
    contacts = models.OneToOneField('Contacts', on_delete=models.CASCADE, verbose_name='Контакты')
    products = models.ForeignKey('Products', on_delete=models.CASCADE, verbose_name='Товар', db_index=True)
    level = models.ForeignKey('self', on_delete=models.CASCADE, verbose_name='Уровень')

    def __str__(self):
        return f'{self.name}- {self.supplier}'

    class Meta:
        verbose_name = 'Поставщик'
        verbose_name_plural = 'Поставщики'


class Contacts(models.Model):
    email = models.EmailField(unique=True, verbose_name="E-mail")
    country = models.CharField(max_length=200, verbose_name="Страна")
    city = models.CharField(max_length=200, verbose_name="Город")
    street = models.CharField(max_length=200, verbose_name="Улица")
    house = models.CharField(max_length=200, verbose_name="Дом")

    class Meta:
        verbose_name = 'Контакты'
        verbose_name_plural = 'Контакты'


class Product(models.Model):
    name = models.CharField(unique=True, max_length=200, verbose_name="Наименование", db_index=True)
    model = models.CharField(unique=True, max_length=200, verbose_name="Модель", db_index=True)
    release_date = models.DateField(auto_now_add=True, verbose_name="Дата выхода продукта", db_index=True)

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
