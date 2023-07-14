from django.shortcuts import render, redirect
from .forms import ProductForm
from .models import Product


# index.html settings.

def productsIndex(request):
    products = Product.objects.all()
    
    context = {
        "products": products,
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


def editProduct(request, pk):
    product = Product.objects.get(pk=pk)

    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('Products')
    else:
        form = ProductForm(instance=product)
    
    context={
        'form': form,
        'product': product
    }

    return render(request, 'index.html', context)


def deleteProduct(request, pk):
    product = Product.objects.get(pk=pk)
    product.delete()
    
    return redirect('Products')


# End index.html settings.


# cartIndex.html settings.

def removeFromCart(request, product_id):
    if 'cart' in request.session:
        cart = request.session.get('cart', [])
        if product_id in cart:
            cart.remove(product_id)
            request.session['cart'] = cart
            request.session.modified = True

    return redirect('cartIndex')


def cartIndex(request):
    product_ids = request.session.get('cart', [])
    products = Product.objects.filter(id__in=product_ids)
    
    context = {
        'products': products,
    }
    
    return render(request, 'cartIndex.html', context)


def addToCart(request, product_id):
    product = Product.objects.get(id=product_id)

    if 'cart' not in request.session:
        request.session['cart'] = []

    cart = request.session['cart']

    cart.append(product_id)

    request.session.modified = True

    return redirect('cartIndex')

# End cartIndex.html settings.