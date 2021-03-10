from django.contrib import admin
from .models import Category
from .models import Product
from .models import Subcategory
from .models import SubcategoryFeature
from .models import Manufacturer
from .models import ProductValues


class ProductValuesInline(admin.TabularInline):
    model = ProductValues
    extra = 1


class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductValuesInline]


class SubcategoryFeatureInline(admin.TabularInline):
    model = SubcategoryFeature
    extra = 1


class SubcategoryAdmin(admin.ModelAdmin):
    inlines = [SubcategoryFeatureInline]


admin.site.register(Category)
admin.site.register(Subcategory, SubcategoryAdmin)
admin.site.register(Manufacturer)
admin.site.register(Product, ProductAdmin)
