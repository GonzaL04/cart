from django.shortcuts import render

# Create your views here.

def productsIndex(request):
    return render (request, 'index.html')