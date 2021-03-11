from .models import Category
from .models import Subcategory
from .models import SubcategoryFeature
from .models import SubcategoryValues
from .models import Product
from .models import ProductItems
from rest_framework import serializers


class ProductItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductItems
        fields = '__all__'

    def to_representation(self, instance):
        print(instance.__dict__)
        return {
            SubcategoryFeature.objects.get(id=instance.feature_id).feature:
            SubcategoryValues.objects.get(id=instance.value_id).value
        }


class ProductSerializer(serializers.ModelSerializer):
    productitems_set = ProductItemsSerializer(many=True)

    class Meta:
        model = Product
        fields = '__all__'


class SubcategorySerializer(serializers.ModelSerializer):
    children = serializers.SerializerMethodField()
    options = serializers.SerializerMethodField()
    class Meta:
        model = Subcategory
        fields = '__all__'

    def get_children(self, obj):
        child = Subcategory.objects.filter(subcategory_parent=obj)
        if not child:
            child = Product.objects.filter(subcategory=obj)

            return [c.product_name for c in child]

        return [c.subcategory_name for c in child]

    def get_options(self, obj):
        opt = []
        
        for option in SubcategoryFeature.objects.filter(subcategory=obj):
            o = {}
            o['optionName'] = option.feature
            o['values'] = []
            for item in SubcategoryValues.objects.filter(subcategoryfeature=option):
                s = {}
                s['value'] = item.value
                s['count'] = Product.objects.filter(productitems__value=item).count()
                o['values'].append(s)
            opt.append(o)

        return opt


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'
