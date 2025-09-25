"""
URL configuration for store_8_09_25 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from products.views.categories import CategoryViewSet
from products.views.suppliers import SupplierViewSet
from products.views.products import ProductDetail1UpdateDeleteView, ProductListCreateView, ProductViewSet
from products.views.product_details import ProductDetailUpdateDeleteView, ProductDetailListCreateView
from products.views.addresses import AddressViewSet
from products.views.customers import CustomerListCreateView, CustomerDetailsUpdateDeleteView, CustomerViewSet
from products.views.orders import OrderListCreateView, OrderDetailUpdateDeleteView
from products.views.orderitems import OrderItemListCreateView, OrderItemDetailUpdateDeleteView

router = DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'suppliers', SupplierViewSet)
router.register(r'addresses', AddressViewSet)
router.register(r'products', ProductViewSet)
router.register(r'customers', CustomerViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)),
    path('api/v1/products/', ProductListCreateView.as_view()),
    path('api/v1/products/<int:pk>/', ProductDetail1UpdateDeleteView.as_view()),
    path('api/v1/product-details/', ProductDetailListCreateView.as_view()),
    path('api/v1/product-details/<int:pk>/', ProductDetailUpdateDeleteView.as_view()),
    path('api/v1/customers/', CustomerListCreateView.as_view()),
    path('api/v1/customer/<int:pk>/', CustomerDetailsUpdateDeleteView.as_view()),
    path('api/v1/orders/', OrderListCreateView.as_view()),
    path('api/v1/orders/<int:pk>/', OrderDetailUpdateDeleteView.as_view()),
    path('api/v1/order-items/', OrderItemListCreateView.as_view()),
    path('api/v1/order-items/<int:pk>/', OrderItemDetailUpdateDeleteView.as_view()),

]
