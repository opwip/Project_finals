from django.db import models
from autoslug import AutoSlugField

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)
    slug = AutoSlugField(populate_from='name', editable=True, always_update=True)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return f"{self.name}"


class Product(models.Model):
    name = models.CharField(max_length=255, unique=True)
    slug = AutoSlugField(populate_from='name', editable=True, always_update=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='products')
    photo = models.ImageField(upload_to="products/", blank=True)
    in_stock = models.BooleanField(default=True)
    desc = models.TextField(blank=True)
    maker = models.CharField(max_length=255, unique=False)

    class Meta:
        verbose_name_plural = "Product"
        unique_together = ['id', 'slug']

    def __str__(self):
        return f"{self.name}"


class OrderItems(models.Model):
    name = models.CharField(max_length=255)
    photo = models.ImageField(upload_to="products/", blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    amount = models.IntegerField()


class Order(models.Model):
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    # basket = models.JSONField(null=False, blank=True)
    basket = models.ForeignKey(OrderItems, on_delete=models.PROTECT, related_name='OrderItems')


