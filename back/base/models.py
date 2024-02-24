from django.db import models
from django.utils.text import slugify

# Create your models here.
class Category(models.Model):
   """
    Defines category model

    """ 
    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=255)

    def save(self, **kwargs):
        """
        saves the slug

        """
        self.slug = slugify(self.name)
        super(Category, self).save(**kwargs)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        """
        returns string representation of a category name

        """
        return f"{self.name}"


class Product(models.Model):
    """
    Defines product model
    """
    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='products')
    photo = models.ImageField(upload_to="products/", blank=True)
    in_stock = models.BooleanField(default=True)
    desc = models.TextField(blank=True)
    maker = models.CharField(max_length=255, unique=False)

    def save(self, **kwargs):
        self.slug = slugify(self.name)
        super(Product, self).save(**kwargs)

    class Meta:
        verbose_name_plural = "Product"
        unique_together = ['id', 'slug']

    def __str__(self):
        """
        returns string representation of a product name

        """
        return f"{self.name}"


class OrderItem(models.Model):
    """
    Defines Items in basket for Order model
    """
    name = models.CharField(max_length=255)
    photo = models.ImageField(upload_to="products/", blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    amount = models.IntegerField()


class Order(models.Model):
    """
    defines order model
    """
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    basket = models.ForeignKey(OrderItem, on_delete=models.PROTECT, related_name='orderItems')

    def total_price(self):
        """calculates total price for items in basket"""
        price = 0
        for item in self.basket:
            price += item.price
        return price



