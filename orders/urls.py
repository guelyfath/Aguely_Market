from django.urls import path
from . import views

# Configuration des URL pour l'application products
urlpatterns = [
    path('', views.cart_view, name='panier'),
    path('checkout/', views.checkout_view, name='checkout'),
    path('order_history/', views.order_history_view, name='order_history'),
]

