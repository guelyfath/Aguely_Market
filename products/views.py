from django.shortcuts import render

# Create your views here.
def category_view(request):
    return render(request,'category.html')

def product_detail_view(request):
    return render(request,'product_detail.html')

def search_results_view(request):
    return render(request,'search_results.html')

def shop_view(request):
    return render(request,'shop.html')