# product_apis/serializers.py
from rest_framework import serializers
from .models import Product, ProductCategory, ProductStatus, Material
from Varient.models import Varient, SizeVariant

class SizeVariantSerializer(serializers.ModelSerializer):
    class Meta:
        model = SizeVariant
        fields = '__all__'

    def to_representation(self, instance):
        print(f"SizeVariant instance data: {instance.__dict__}")  # Debug print
        return super().to_representation(instance)

class VarientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Varient
        fields ='__all__'

class ProductCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCategory
        fields = ['category_id', 'category_title']

class ProductStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductStatus
        fields = ['status_id', 'status_name']

class MaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Material
        fields = ['material_id', 'material_title']

class ProductSerializer(serializers.ModelSerializer):
    category = ProductCategorySerializer()
    material = MaterialSerializer()
    status = ProductStatusSerializer()
    size_variants = SizeVariantSerializer(many=True)
    variants = VarientSerializer(many=True)

    class Meta:
        model = Product
        fields = '__all__'
    
    def to_representation(self, instance):
        print(f"Product ID: {instance.product_id}")  # Debug print
        print(f"Size Variants: {list(instance.size_variants.all())}")  # Debug print
        data = super().to_representation(instance)
        print(f"Serialized data: {data}")  # Debug print
        return data