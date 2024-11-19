from django.urls import path
from .views import ProductList

urlpatterns = [
    path('product/', ProductList.as_view(),name='product-detail'),
]
