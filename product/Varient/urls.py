from django.urls import path
from . import views

urlpatterns = [

    #size varient
    path('create-varient/', views.SizeVariantListCreate.as_view(), name='create-varient'),#create size varient
    path('size-variants/', views.SizeVariantListCreate.as_view(), name='sizevariant-detail'),  #list all varient size
    path('size-variants/<int:pk>/', views.SizeVariantListCreate.as_view(), name='sizevariant-detail'),  # For a specific size variant/update/delete
    

    #varient
    path('varient/', views.VariantListCreate.as_view(), name='create-varient'),#create size varient
    path('varient/<int:pk>/', views.VariantListCreate.as_view(), name='varient-detail'),  #list all varient
]