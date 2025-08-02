from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, SalesReportViewSet

router = DefaultRouter()
router.register(r'sales_report', SalesReportViewSet, basename='sales_report')
router.register(r'', ProductViewSet, basename='products')


urlpatterns = [
    path('', include(router.urls)),
]
