from django.urls import path
from . import views

# Configuration des URL pour l'application vendors
urlpatterns = [ 
    path('', views.become_vendor_view, name='devenir_vendeur'),
    path('magasin_vendeur', views.vendor_store_view, name='magasin_vendeur'),
    path('vendor-dashboard/', views.vendor_dashboard_view, name='vendor_dashboard'),
    path('add-product/', views.add_product_view, name='add_product'),
    path('edit-product/<int:product_id>/', views.edit_product_view, name='edit_product'),
]
