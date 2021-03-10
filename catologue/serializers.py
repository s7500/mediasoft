from .models import Category
from .models import Subcategory
from .models import Product
from .models import ProductValues
from rest_framework import serializers


class ProductValuesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductValues
        fields = '__all__'

    def to_representation(self, instance):
        return {instance.feature.feature: instance.value}


class ProductSerializer(serializers.ModelSerializer):
    productvalues_set = ProductValuesSerializer(many=True)

    class Meta:
        model = Product
        fields = '__all__'


class SubcategorySerializer(serializers.ModelSerializer):
    quantity = serializers.SerializerMethodField()

    class Meta:
        model = Subcategory
        fields = '__all__'

    def get_quantity(self, obj):
        return Product.objects.filter(subcategory=obj).count()


class CategorySerializer(serializers.ModelSerializer):
    subcategory_set = SubcategorySerializer(many=True)

    class Meta:
        model = Category
        fields = '__all__'
