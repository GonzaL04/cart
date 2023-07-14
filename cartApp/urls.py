from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('', views.productsIndex, name="Products"),
    path('addProduct/', views.addProduct, name='addProduct'),
    path('edit/<int:pk>/', views.editProduct, name='editProduct'),
    path('deleteProduct/<int:pk>/', views.deleteProduct, name='deleteProduct'),
    path('cart/remove/<int:product_id>/', views.removeFromCart, name='removeFromCart'),
    path('cart/', views.cartIndex, name="cartIndex"),
    path('cart/add/<int:product_id>/', views.addToCart, name='addToCart'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)