# content/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('menu_items/', views.MenuCategoryListView.as_view(), name='menu_item_list'),
]
