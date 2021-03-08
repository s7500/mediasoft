from django.db import models
import uuid


class Category(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    category_name = models.SlugField()

    def __str__(self):
        return self.category_name


class Subcategory(models.Model):
    catergory = models.ForeignKey(Category, on_delete=models.CASCADE)
    subcategory_name = models.TextField(default=None)

    def __str__(self):
        return self.subcategory_name


class Manufacturer(models.Model):
    manufacturer_name = models.TextField(default=None)

    def __str__(self):
        return self.manufacturer_name


class Product(models.Model):
    subcategory = models.ForeignKey(Subcategory, on_delete=models.CASCADE)
    product_name = models.TextField()
    price = models.IntegerField(default=None)
    manufacturer = models.ForeignKey(
                    Manufacturer, 
                    on_delete=models.PROTECT, 
                    blank=True
                )

    def __str__(self):
        return self.product_name


class ProductFields(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    feature = models.TextField()
    value = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.feature}: {self.value}'
