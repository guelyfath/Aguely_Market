from django.urls import path
from . import views

# Configuration des URL pour l'application pages
urlpatterns = [ 
    path('', views.home_view, name='home'),
    path('contact/', views.contact_view, name='contact'),
    path('a-propos/', views.about_view, name='about'),
]