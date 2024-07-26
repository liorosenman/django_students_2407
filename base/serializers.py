from rest_framework import serializers
from .models import Product, Student

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class StudentSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(source='user.id', read_only=True)
    password = serializers.CharField(source='user.password', write_only=True)
    is_superuser = serializers.BooleanField(source='user.is_superuser', read_only=True)
    username = serializers.CharField(source='user.username', read_only=True)
    is_active = serializers.BooleanField(source='user.is_active', read_only=True)
    first_name = serializers.CharField(source='user.first_name', read_only=True)
    email = serializers.EmailField(source='user.email', read_only=True)
    
    class Meta:
        model = Student
        fields = "__all__"
        # fields = ['id', 'password', 'image', 'email', 'profession', 'stage', 'university']



