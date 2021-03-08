from django.contrib import admin
from django.urls import path, include, re_path
from catologue import views
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'categories', views.CategoryViewSet)
# router.register(r'products', views.ProductList, basename='products',)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    re_path(r'^api/products/((?P<feature>.+)\=(?P<value>.+))/$', views.ProductList.as_view(),)
]
