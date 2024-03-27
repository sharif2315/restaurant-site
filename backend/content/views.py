from rest_framework import generics
from .models import MenuCategory, MenuItem
from .serializers import MenuCategorySerializer 
# , MenuItemSerializer, MenuItemWithCategorySerializer


# class MenuItemListView(generics.ListAPIView):
#     queryset = MenuItem.objects.all()
#     serializer_class = MenuItemSerializer


# class MenuItemListView(generics.ListAPIView):
#     queryset = MenuItem.objects.all()
#     serializer_class = MenuItemWithCategorySerializer


class MenuCategoryListView(generics.ListAPIView):
    queryset = MenuCategory.objects.all()
    serializer_class = MenuCategorySerializer