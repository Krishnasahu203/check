from django.contrib import admin
from .models import ProductCategory, ProductStatus, Material, Product

admin.site.register(ProductCategory)
admin.site.register(ProductStatus)

admin.site.register(Material)   
admin.site.register(Product)

# Register your models here.
