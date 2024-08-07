from django.db import models

from users.models import User

NULLABLE = {"blank": True, "null": True}


class Product(models.Model):

    # STATUS_CHOICES = (
    #     ("new", "Новый"),
    #     ("in_stock", "В наличии"),
    #     ("out_of_stock", "Нет в наличии"),
    # )

    name = models.CharField(max_length=100, verbose_name="Наименование")
    description = models.TextField(verbose_name="Описание")
    image = models.ImageField(
        upload_to="products/images", verbose_name="Изображение (превью)", **NULLABLE
    )
    category = models.ForeignKey(
        "Category",
        on_delete=models.CASCADE,
        verbose_name="Категория",
        related_name="products",
    )
    price = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name="Цена за покупку"
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(
        auto_now=True, verbose_name="Дата последнего изменения"
    )
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, verbose_name='Владелец', **NULLABLE)
    is_published = models.BooleanField(default=False, verbose_name="Опубликовано")
    # is_published = models.CharField(verbose_name="Опубликовано", choices=STATUS_CHOICES)

    def __str__(self):
        return f"{self.name}, {self.description}, {self.price}"

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
        ordering = ["name", "price"]
        permissions = [
            ("can_edit_description", "Может менять описание продукта"),
            ("can_cancel_publishing", "Может отменять публикацию продукта"),
            ("can_change_category", "Может менять категорию продукта")
        ]


class Category(models.Model):

    name = models.CharField(max_length=100, verbose_name="Наименование")
    description = models.TextField(verbose_name="Описание")

    def __str__(self):
        return f"{self.name}, {self.description}"

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"



class Version(models.Model):

    product = models.ForeignKey(
        Product,
        on_delete=models.SET_NULL,
        **NULLABLE,
        verbose_name="Версия",
        related_name="version_product",
    )

    number_version = models.CharField(default=0, verbose_name="Номер версии")
    name_version = models.CharField(max_length=100, verbose_name="Наименование версии")
    is_current = models.BooleanField(
        default=True, verbose_name="Признак текущей версии"
    )

    def __str__(self):
        return f"{self.number_version}, {self.name_version}"

    class Meta:
        verbose_name = "Версия"
        verbose_name_plural = "Версии"
