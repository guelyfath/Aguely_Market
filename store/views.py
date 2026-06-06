from django.shortcuts import render
from .models import Product

# Creation des vues de l'application

def home_view(request):
    return render(request,'index.html')

def boutique_view(request):
    products = Product.objects.all()
    return render(request, 'boutique.html', {'products': products})


def compte_view(request):
    return render(request,'compte.html')

def inscription_view(request):
    return render(request,'inscription.html')

def vendeur_view(request):
    return render(request,'vendeur.html')


def produit_view(request):
    return render(request,'produit.html')


def panier_view(request):
    return render(request,'panier.html')

# Affichage des produits dans la boutique

def index(request):
    products = Product.objects.all()
    return render(request, 'index.html', {'products': products})

