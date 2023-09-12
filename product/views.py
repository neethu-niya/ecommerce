from rest_framework import viewsets
from .models import Product
from django.contrib.auth.models import User
from .serializers import ProductSerializer,UserSerializer,ProductActivationSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.utils import timezone
from datetime import timedelta


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    def get_queryset(self):
        user = self.request.user
        queryset = Product.objects.filter(owner=user)
        return queryset



    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
        
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def perform_create(self, serializer):
        user = serializer.save()
        group_name = 'customer'
        group = Group.objects.get(name=group_name)
        user.groups.add(group)  



