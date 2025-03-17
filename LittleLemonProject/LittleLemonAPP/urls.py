from django.urls import path
from . import views

urlpatterns = [
    path('category', views.CategoryView.as_view()),
    path('menu-items', views.MenuItemView.as_view()),
    path('cart', views.CartView.as_view()),
    path('orders', views.OrderView.as_view()),
    path('order-items', views.OrderItemView.as_view()),
]
