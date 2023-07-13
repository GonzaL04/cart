from django.urls import path
from . import views

urlpatterns = [
    path('', views.productsIndex, name="Products"),
    path('addProduct/', views.addProduct, name='addProduct'),
    path('deleteProduct/<int:pk>/', views.deleteProduct, name='deleteProduct'),
]