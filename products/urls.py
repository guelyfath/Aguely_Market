from django.urls import path
from . import views

# Configuration des URL pour l'application products
urlpatterns = [
    path('', views.shop_view, name='boutique'),
    path('category/<int:category_id>/', views.category_view, name='category'),
    path('product/<int:product_id>/', views.product_detail_view, name='product_detail'),
    path('search/', views.search_results_view, name='search_results'),
]
