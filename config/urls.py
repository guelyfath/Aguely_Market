from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static
from django.conf import settings

# Configuration des URL pour l'application store

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include('pages.urls')),
    path('accounts/', include('accounts.urls')),
    path('products/', include('products.urls')),
    path('vendors/', include('vendors.urls')),
    path('orders/', include('orders.urls')),
]

# Configuration pour servir les fichiers médias en développement
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

