from django.contrib import admin
from django.urls import path, include, re_path
from catologue import views
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'categories', views.CategoriesViewSet, basename='category-list')
router.register(r'subcategory', views.SubcategoryList, basename='subcategory-list')
router.register(r'product', views.ProductDetail, basename='product-detail')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    re_path(r'^api/products/$', views.ProductList.as_view()),
    re_path(r'^api/products/((?P<feature>\w+)\=(?P<value>\w+))/$', views.ProductList.as_view())
]
