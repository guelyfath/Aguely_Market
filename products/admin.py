from django.contrib import admin

from .models import Produit
# Register your models here.


@admin.register(Produit)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "price", "stock")
    search_fields = ("name",)
    list_filter = ("stock",)
