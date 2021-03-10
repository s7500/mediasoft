from django.db import models
import uuid


class Category(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    category_name = models.SlugField()

    def __str__(self):
        return self.category_name


class Subcategory(models.Model):
    catergory = models.ForeignKey(
                    Category, 
                    on_delete=models.CASCADE, 
                    blank=True,
                    null=True,
                    default = None,
                )
    subcategory_parent = models.ForeignKey(
                            'self', 
                            on_delete=models.CASCADE, 
                            null=True,
                            default = None,
                            blank = True
                        )
    subcategory_name = models.CharField(max_length = 32)

    def __str__(self):
        return self.subcategory_name


class SubcategoryFeature(models.Model):
    subcategory = models.ForeignKey(Subcategory, on_delete=models.CASCADE)
    feature = models.CharField(max_length = 32)

    def __str__(self):
        return self.feature


class Manufacturer(models.Model):
    manufacturer_name = models.CharField(max_length=32, default=None)

    def __str__(self):
        return self.manufacturer_name


class Product(models.Model):
    subcategory = models.ForeignKey(Subcategory, on_delete=models.CASCADE)
    product_name = models.CharField(max_length = 32)
    manufacturer = models.ForeignKey(
                    Manufacturer, 
                    on_delete=models.PROTECT, 
                    blank=True
                )

    def __str__(self):
        return self.product_name


class ProductValues(models.Model):
    feature = models.ForeignKey(SubcategoryFeature, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    value = models.CharField(max_length = 32, blank=True)

    def __str__(self):
        return f'{self.feature.feature}: {self.value}'