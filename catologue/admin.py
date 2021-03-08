from django.contrib import admin
from .models import Category
from .models import Product
from .models import Subcategory
from .models import Manufacturer
from .models import ProductFields


class ProductFieldsInline(admin.TabularInline):
    model = ProductFields
    extra = 1


class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductFieldsInline]


admin.site.register(Category)
admin.site.register(Subcategory)
admin.site.register(Manufacturer)
admin.site.register(Product, ProductAdmin)
