import django_filters.rest_framework
from rest_framework import viewsets, generics
from .serializers import CategorySerializer
from .serializers import SubcategorySerializer
from .serializers import ProductSerializer
from .models import Category
from .models import Subcategory
from .models import Product


class ProductList(generics.ListAPIView):
    serializer_class = ProductSerializer
    filterset_fields = '__all__'
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]

    def get_queryset(self):
        queryset = Product.objects.all()
        feature = self.kwargs.get('feature', None)
        value = self.kwargs.get('value', None)
        if feature and value:
            queryset = Product.objects.filter(
                        productitems__feature__feature=feature,
                        productitems__value__value=value
                    )

        return queryset


class ProductDetail(viewsets.ModelViewSet):
    serializer_class = ProductSerializer

    def get_queryset(self):
        id = self.kwargs.get('pk')
        queryset = Product.objects.filter(id=id)
        
        return queryset


class CategoriesViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    

class SubcategoryList(viewsets.ModelViewSet):
    """
    idk what hell is going on
    This is view o to return all subcategoty belong the category, but it isn't
    """
    serializer_class = SubcategorySerializer
    queryset = Subcategory.objects.all()


