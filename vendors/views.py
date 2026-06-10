from django.shortcuts import render

# Create your views here.

def add_product_view(request):
    return render(request,'add_product.html')

def become_vendor_view(request):
    return render(request,'become_vendor.html')

def edit_product_view(request):
    return render(request,'edit_product.html')

def vendor_store_view(request):
    return render(request,'vendor_store.html')

def vendor_dashboard_view(request):
    return render(request,'vendor_dashboard.html')