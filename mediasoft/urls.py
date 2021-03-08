from django.contrib import admin
from django.urls import path, include
from catologue import views
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'categories', views.CategoryViewSet)
router.register(r'products', views.ProductViewSet, basename='products',)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
