from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('all-products/', views.all_products, name='all-products'),
    path('product-detail/<str:pk>', views.product_detail, name='product-detail'),
]
