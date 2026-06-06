from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from store import views

# Configuration des URL pour l'application store
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home_view, name='Accueil'),
    path('compte/', views.compte_view, name='compte'),
    path('inscription/', views.inscription_view, name='inscription'),
    path('vendeur/', views.vendeur_view, name='vendeur'),
    path('boutique/', views.boutique_view, name='boutique'),
    path('produit/', views.produit_view, name='produit'),
    path('panier/', views.panier_view, name='panier'),
]

# Configuration pour servir les fichiers médias en développement
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
