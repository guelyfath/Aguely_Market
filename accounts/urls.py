from django.urls import path
from . import views

# Configuration des URL pour l'application vendors
urlpatterns = [ 
    path('', views.login_view, name='connexion'),
    path('supprimer-mdp/', views.password_reset_view, name='supprimer-mdp'),
    path('profile/', views.profile_view, name='profile'),
    path('inscription/', views.register_view, name='inscription'),
]