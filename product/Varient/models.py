from django.db import models


class SizeVariant(models.Model):
    product = models.ForeignKey('product_apis.Product', on_delete=models.CASCADE)
    price_with_shipping = models.DecimalField(
        max_digits=10, 
        decimal_places=2, 
        null=True,
        blank=True,
        verbose_name="Price (with shipping cost)"
    )
    add_size = models.BooleanField(default=False, verbose_name="Add Size Variant")
    size = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    shipping_cost = models.DecimalField(max_digits=6, decimal_places=2, default=0.0)  # Added shipping_cost field
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Size Variant"
        verbose_name_plural = "Size Variants"

    def save(self, *args, **kwargs):
        if self.price_with_shipping is None:  # If no shipping cost is provided
            self.price_with_shipping = self.price + self.shipping_cost  # Calculate price with shipping cost
        super(SizeVariant, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.size} - ₹{self.price}"
    



class Varient(models.Model):
    Product = models.ForeignKey('product_apis.Product', on_delete=models.CASCADE)
    # If this is the "variant group" (edit_variant)
    add_variant = models.BooleanField(default=True)  # Whether variant is added
    enter_variant_name = models.CharField(max_length=100, blank=True, null=True)  # Name for the variant group (formerly variant_group_name)
    
    # For each individual variant
    image = models.ImageField(upload_to='variant_images/', null=True, blank=True)  # Image for the variant item
    variant_name = models.CharField(max_length=100)  # Name of the variant item (e.g., 'Red', 'Large')
    is_active = models.BooleanField(default=True)  # Whether the variant item is active
    
    

    def __str__(self):
        
        return self.variant_name
