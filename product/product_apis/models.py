
from django.db import models
from Varient.models import Varient, SizeVariant


class Occasion(models.Model):
    occasion_id = models.BigAutoField(primary_key=True)  # Auto-increment primary key
    occasion_title = models.CharField(max_length=250)  
    parent_id = models.ForeignKey(
        'self',                   # Reference to the same model (self-referential)
        on_delete=models.SET_NULL, # If the parent is deleted, set the field to NULL
        null=True,                 # Can be NULL, meaning the occasion doesn't have a parent
        blank=True,                # Optional field in forms
        related_name='sub_occasions', # Reverse relation from parent to children
        db_column='parent_id'      # Use parent_id as the column name in the database
    )

    #same path for occasion
    short_description = models.CharField(max_length=250, null=True, blank=True)  # Optional field
    image_url = models.CharField(max_length=1000, null=True, blank=True)  # Optional field
    is_active = models.BooleanField(default=True)  # Corresponds to tinyint(1)
    created_at = models.DateTimeField(auto_now_add=True)  # Automatically set when the object is created
    created_by = models.BigIntegerField()  # Assuming this is a user or system ID
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)  # Automatically set when updated
    updated_by = models.BigIntegerField(null=True, blank=True)  # Optional, assuming a user or system ID

    class Meta:
        db_table = 'mst_occasion'  # Table name in the database
        indexes = [
            models.Index(fields=['parent_id']),  # Index for parent_id foreign key
        ]
    
    def __str__(self):
        return self.occasion_title

class ProductCategory(models.Model):
    category_id = models.BigAutoField(primary_key=True)
    category_title = models.CharField(max_length=250)
    parent_id = models.ForeignKey(
        'self',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='child_categories',
    )
    short_description = models.CharField(max_length=1000, null=True, blank=True)
    subcategories = models.JSONField(default=list, blank=True)  # This will store subcategory references
    path = models.CharField(max_length=500, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=8)
    updated_at = models.DateTimeField(null=True, blank=True, auto_now=True)
    updated_by = models.CharField(max_length=8, null=True, blank=True)

    class Meta:
        db_table = 'mst_product_category'
        ordering = ['category_id']
        unique_together = ['category_title', 'parent_id']

    def __str__(self):
        return self.category_title

    def save(self, *args, **kwargs):
        # For root categories (no parent), set subcategories as empty list and parent_id as null
        if not self.parent_id:
            self.subcategories = []  # Root categories have an empty subcategory list
        else:
            # If the category has a parent, update the subcategories field
            self.subcategories = [self.parent_id.category_id, self.category_id]
        
        # Generate path based on parent category
        if self.parent_id:
            self.path = f"{self.parent_id.path},{self.category_title}"
        else:
            self.path = self.category_title

        super(ProductCategory, self).save(*args, **kwargs)




# ProductStatus Model
class ProductStatus(models.Model):
    status_id = models.AutoField(primary_key=True)
    status_name = models.CharField(max_length=25)
    is_active = models.BooleanField(default=True)

    class Meta:
        db_table = 'mst_product_status'

    def __str__(self):
        return self.status_name





# Material Model (Representing mst_material table)
class Material(models.Model):
    material_id = models.BigAutoField(primary_key=True)
    material_title = models.CharField(max_length=100)
    short_description = models.CharField(max_length=250, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.BigIntegerField()
    updated_at = models.DateTimeField(null=True, blank=True, auto_now=True)
    updated_by = models.BigIntegerField(null=True, blank=True)

    class Meta:
        db_table = 'mst_material'
        indexes = [
            models.Index(fields=['is_active']),
            models.Index(fields=['material_title']),
        ]

    def __str__(self):
        return self.material_title


# Product Model
class Product(models.Model):
    product_id = models.BigAutoField(primary_key=True)
    store_id = models.CharField(max_length=8, null=True)
    user_id = models.CharField(max_length=8, null=True)
    product_title = models.CharField(max_length=500)
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE, related_name='products', null=True, blank=True)

    relevent_Category_id = models.ManyToManyField(ProductCategory, blank=True)
    is_customisable = models.BooleanField()
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    selling_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    discount_perc = models.DecimalField(max_digits=4, decimal_places=2, default=0.00)
    discount_amt = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    description = models.CharField(max_length=1000, null=True, blank=True)
    height = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    width = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    length = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    weight = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    # Relationship with Material (Foreign Key)
    material = models.ForeignKey(Material, null=True, blank=True, on_delete=models.SET_NULL)
    material_name = models.CharField(max_length=250, null=True, blank=True)
    color_variants = models.CharField(max_length=500, null=True, blank=True)
    surface = models.CharField(max_length=100, null=True, blank=True)
    other_details = models.CharField(max_length=500, null=True, blank=True)

    has_size_variant = models.BooleanField(default=False)
    has_color_variant = models.BooleanField(default=False)
    variant_title = models.CharField(max_length=100, null=True, blank=True)
    is_personalised = models.BooleanField(default=False)
    personalisation_note = models.CharField(max_length=500, null=True, blank=True)

    # Relationship with ProductStatus (Foreign Key)
    status = models.ForeignKey(ProductStatus, on_delete=models.CASCADE, null=True, blank=True)
    status_reason = models.CharField(max_length=500, null=True, blank=True)


    size_variants = models.ManyToManyField(SizeVariant, related_name='products', blank=True)
    variants = models.ManyToManyField(Varient, related_name='products',blank=True)

    admin_rating = models.DecimalField(max_digits=4, decimal_places=2, default=0.00)
    public_rating = models.DecimalField(max_digits=4, decimal_places=2, default=0.00)
    total_viewed_count = models.IntegerField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=8)
    updated_at = models.DateTimeField(auto_now=True)
    updated_by = models.CharField(max_length=8)
    isapproved = models.BooleanField(default=False)
    isdisapproved = models.BooleanField(default=False)

    is_active = models.BooleanField(default=False)
    is_deleted = models.BooleanField(default=False)
    deleted_at = models.DateTimeField(null=True, blank=True)
    deleted_by = models.CharField(max_length=8, null=True, blank=True)

    class Meta:
        db_table = 'mst_products'
        indexes = [
            models.Index(fields=['status']),
            models.Index(fields=['category']),
            models.Index(fields=['material']),
        ]

    def __str__(self):
        return self.product_title


# class ProductColor(models.Model):
#     color_variant_id = models.BigAutoField(primary_key=True)
#     product_id = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='colors')
#     color_name = models.CharField(max_length=50)
#     product_image_id = models.BigIntegerField()
#     is_active = models.BooleanField(default=True)

#     class Meta:
#         db_table = 'mst_product_color'


