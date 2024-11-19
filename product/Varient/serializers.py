from .models import Varient,SizeVariant

from rest_framework import serializers


class VariantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Varient
        fields = ['id', 'add_variant', 'enter_variant_name', 'variant_name', 'image', 'is_active']

    def validate_add_variant(self, value):
        if not value:
            raise serializers.ValidationError("Variant cannot be added if 'add_variant' is false.")
        return value


class SizeVariantSerializer(serializers.ModelSerializer):
    class Meta:
        model = SizeVariant
        fields = '__all__'