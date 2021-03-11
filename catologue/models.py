from django.db import models
import uuid


class Category(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    category_name = models.SlugField(unique=True)

    def __str__(self):
        return self.category_name


class Subcategory(models.Model):
    category = models.ForeignKey(
                    Category, 
                    on_delete=models.CASCADE,
                    to_field = 'category_name',
                    blank=True,
                    null=True,
                    default = None
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


class SubcategoryValues(models.Model):
    subcategoryfeature = models.ForeignKey(SubcategoryFeature, on_delete=models.CASCADE)
    value = models.CharField(max_length = 32)
    
    def __str__(self):
        return self.value



class Product(models.Model):
    subcategory = models.ForeignKey(Subcategory, on_delete=models.CASCADE)
    product_name = models.CharField(max_length = 32)

    def __str__(self):
        return self.product_name


class ProductItems(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    feature = models.ForeignKey(SubcategoryFeature, on_delete=models.CASCADE)
    value = models.ForeignKey(SubcategoryValues, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.feature.feature}: {self.value.value}'