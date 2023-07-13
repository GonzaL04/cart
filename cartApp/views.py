from django.shortcuts import render, redirect
from .forms import ProductForm
from .models import Product

# Create your views here.

def productsIndex(request):
    products = Product.objects.all()
    context = {
        "products": products
    }
    return render (request, 'index.html', context)

def addProduct(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('Products')
    else:
        form = ProductForm()
    
    return render(request, 'index.html', {'form': form})

def deleteProduct(request, pk):
    product = Product.objects.get(pk=pk)
    product.delete()
    return redirect('Products')