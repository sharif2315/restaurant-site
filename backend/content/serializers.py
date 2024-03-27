# serializers.py
from rest_framework import serializers
from .models import MenuCategory, MenuItem


# class MenuCategorySerializer(serializers.ModelSerializer):
#     class Meta:
#         model = MenuCategory
#         fields = '__all__'


# class MenuItemSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = MenuItem
#         fields = '__all__'


# class MenuItemWithCategorySerializer(serializers.ModelSerializer):
#     category_name = serializers.CharField(source='category.name', read_only=True)
#     category_description = serializers.CharField(source='category.description', read_only=True)
#     class Meta:
#         model = MenuItem
#         fields = ['id', 'name', 'description', 'price', 'category', 'category_name', 'category_description']


class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = ['id', 'name', 'description', 'price']

class MenuCategorySerializer(serializers.ModelSerializer):
    menu_items = MenuItemSerializer(many=True, read_only=True)

    class Meta:
        model = MenuCategory
        fields = ['id', 'name', 'description', 'menu_items']