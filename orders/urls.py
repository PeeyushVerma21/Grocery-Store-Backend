from django.urls import path
from .views import (
    CartItemListCreateView, CartItemDeleteView, CheckoutView,
    WishlistListCreateView
)

urlpatterns = [
    path('cart/', CartItemListCreateView.as_view(), name='cart-list-create'),
    path('cart/<int:id>/', CartItemDeleteView.as_view(), name='cart-delete'),
    path('checkout/', CheckoutView.as_view(), name='checkout'),
    path('wishlist/', WishlistListCreateView.as_view(), name='wishlist'),
]
