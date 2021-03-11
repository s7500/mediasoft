from django.contrib import admin
from .models import Category
from .models import Product
from .models import Subcategory
from .models import SubcategoryFeature
from .models import SubcategoryValues
from .models import ProductItems


class ProductItemsInline(admin.TabularInline):
    model = ProductItems
    extra = 1


class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductItemsInline]


class SubcategoryValuesInline(admin.TabularInline):
    model = SubcategoryValues


class SubcategoryFeatureAdmin(admin.ModelAdmin):
    inlines = [SubcategoryValuesInline]


admin.site.register(Category)
admin.site.register(Subcategory)
admin.site.register(SubcategoryFeature, SubcategoryFeatureAdmin)
admin.site.register(Product, ProductAdmin)
