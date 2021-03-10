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
        print(feature, value)
        if feature and value:
            queryset = Product.objects.filter(
                        productvalues__feature__feature=feature,
                        productvalues__value=value
                    )

        return queryset


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filterset_fields = '__all__'
    