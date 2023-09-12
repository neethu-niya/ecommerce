from django.utils import timezone
from rest_framework import serializers
from .models import Product
from django.contrib.auth.models import User

class ProductSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Product
        fields = '__all__'
    
    def validate(self, data):
        instance = getattr(self, 'instance', None)
        if instance:
            if 'active' in data:
                threshold_date = timezone.now() - timezone.timedelta(days=60)
                if not data.get("active") and  instance.registration_date > threshold_date:
                    raise serializers.ValidationError("Cannot change status of a product created less than 2 months ago.")
        return data

class ProductStatusSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Product
        fields = '__all__'
        extra_kwargs = {'active': {'read_only': True}}
 
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password', 'first_name', 'email')
        extra_kwargs = {'password': {'write_only': True}}
class ProductActivationSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    active = serializers.BooleanField()