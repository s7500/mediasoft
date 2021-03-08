from .models import Category
from .models import Subcategory
from .models import Product
from .models import ProductFields
from rest_framework import serializers


class ProductFieldsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductFields
        fields = '__all__'

    def to_representation(self, instance):
        return {instance.feature: instance.value}


class ProductSerializer(serializers.ModelSerializer):
    productfields_set = ProductFieldsSerializer(many=True)

    class Meta:
        model = Product
        fields = '__all__'


class SubcategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Subcategory
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    subcategory_set = SubcategorySerializer(many=True)

    class Meta:
        model = Category
        fields = '__all__'
