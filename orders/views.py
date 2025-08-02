from rest_framework import generics, status
from rest_framework.response import Response
from .models import CartItem, Wishlist, Order, OrderItem
from .serializers import CartItemSerializer, WishlistSerializer, OrderSerializer
from products.models import Product

class CartItemListCreateView(generics.ListCreateAPIView):
    serializer_class = CartItemSerializer

    def get_queryset(self):
        return CartItem.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class CartItemDeleteView(generics.DestroyAPIView):
    serializer_class = CartItemSerializer
    lookup_field = 'id'

    def get_queryset(self):
        return CartItem.objects.filter(user=self.request.user)

class CheckoutView(generics.CreateAPIView):
    serializer_class = OrderSerializer

    def create(self, request, *args, **kwargs):
        cart_items = CartItem.objects.filter(user=request.user)

        if not cart_items.exists():
            return Response({"detail": "Cart is empty."}, status=status.HTTP_400_BAD_REQUEST)

        total = sum(item.product.price * item.quantity for item in cart_items)
        order = Order.objects.create(user=request.user, total_price=total)

        # Create OrderItem for each CartItem
        for item in cart_items:
            OrderItem.objects.create(
                order=order,
                product=item.product,
                quantity=item.quantity,
                price_at_purchase=item.product.price,
            )
            # Update product stock and sold count
            item.product.stock -= item.quantity
            item.product.sold_count += item.quantity
            item.product.save()

        # Delete cart items after copying data
        cart_items.delete()

        serializer = self.get_serializer(order)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class WishlistListCreateView(generics.ListCreateAPIView):
    serializer_class = WishlistSerializer

    def get_queryset(self):
        return Wishlist.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
