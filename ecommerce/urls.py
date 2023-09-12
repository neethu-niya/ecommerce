from django.urls import path, include
from rest_framework.routers import DefaultRouter
from product.views import ProductViewSet,UserViewSet
from django.contrib import admin


router = DefaultRouter()
router.register(r'products', ProductViewSet)
router.register(r'users', UserViewSet)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
   
]
