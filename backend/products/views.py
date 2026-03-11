from django.shortcuts import render
from django.views import View
from .data import products

# Create your views here.

class ProductListView(View):
    def get(self, request):
        context = {
            'produits': products
        }
        return render(request, 'products/product_list.html', context)
