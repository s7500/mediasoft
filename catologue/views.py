from rest_framework import viewsets
from .serializers import CategorySerializer
from .serializers import SubcategorySerializer
from .serializers import ProductSerializer
from .models import Category
from .models import Subcategory
from .models import Product


class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    filterset_fields = '__all__'

    def get_queryset(self):
        queryset = Product.objects.all()
        return queryset
    # def get_queryset(self, *args, **kwargs):
    #     queryset = Product.objects.all()
    #     feature = self.kwargs['feature']
    #     value = self.kwargs['value']
    #     if feature and value:
    #         queryset = Product.objects.filter(
    #                     productfields__feature=feature,
    #                     productfields__value=value
    #                 )

    #     return queryset


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filterset_fields = '__all__'


class ViewSet(viewsets.ModelViewSet):
    queryset = Subcategory.objects.all()
    serializer_class = CategorySerializer
    filterset_fields = '__all__'
    
