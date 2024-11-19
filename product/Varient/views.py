from django.shortcuts import render



# Create your views here.

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import SizeVariant,Varient
from .serializers import   VariantSerializer,SizeVariantSerializer



class SizeVariantListCreate(APIView):
    def post(self, request):
        serializer = SizeVariantSerializer(data=request.data)
        if serializer.is_valid():
            add_size = serializer.validated_data.get('add_size', False)
            
            if not add_size:  # If add_size is False, don't allow creating this variant
                return Response({"error": "This size variant cannot be added."}, 
                                 status=status.HTTP_400_BAD_REQUEST)
            
            # Save the valid data to the database
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

    def get(self, request, pk=None):
        if pk:  # If pk is provided, fetch a particular SizeVariant
            try:
                size_variant = SizeVariant.objects.get(pk=pk)
                serializer = SizeVariantSerializer(size_variant)
                return Response(serializer.data)
            except SizeVariant.DoesNotExist:
                return Response({"error": "SizeVariant not found"}, status=status.HTTP_404_NOT_FOUND)
        else:  # If no pk is provided, return all SizeVariants
            size_variants = SizeVariant.objects.all()
            serializer = SizeVariantSerializer(size_variants, many=True)
            return Response(serializer.data)

    def put(self, request, pk=None):
        if pk:  # If pk is provided, update a particular SizeVariant
            try:
                size_variant = SizeVariant.objects.get(pk=pk)
                
                # Check if the `add_size` field is False, and return an error if it is
                if not size_variant.add_size:
                    return Response({"error": "This size variant cannot be updated as `add_size` is False."}, 
                                     status=status.HTTP_400_BAD_REQUEST)
                
                # Update the object with the provided data
                serializer = SizeVariantSerializer(size_variant, data=request.data, partial=True)
                if serializer.is_valid():
                    serializer.save()  # Save the updated data to the database
                    return Response(serializer.data, status=status.HTTP_200_OK)
                
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            
            except SizeVariant.DoesNotExist:
                return Response({"error": "SizeVariant not found"}, status=status.HTTP_404_NOT_FOUND)
        
        return Response({"error": "SizeVariant ID is required to update a SizeVariant."},status=status.HTTP_400_BAD_REQUEST)
    

    def delete(self, request, pk=None):
        if pk:  # If pk is provided, delete a particular SizeVariant
            try:
                size_variant = SizeVariant.objects.get(pk=pk)                
                size_variant.delete()  # Delete the object from the database
                return Response({"message": "SizeVariant deleted successfully"}, status=status.HTTP_200_OK)
            
            except SizeVariant.DoesNotExist:
                return Response({"error": "SizeVariant not found"}, status=status.HTTP_404_NOT_FOUND)
            




# class VariantListCreate(APIView):
    
    
#     def post(self, request):
#         serializer = VariantSerializer(data=request.data)
#         if serializer.is_valid():
#             if not serializer.validated_data.get('add_variant', False):
#                 return Response({"error": "This variant cannot be added."}, 
#                                  status=status.HTTP_400_BAD_REQUEST)
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

#     def get(self, request, pk=None):
#         if pk:  # If pk is provided, fetch a particular Variant        
#             try:
#                 variant = Varient.objects.get(pk=pk)
#                 serializer = VariantSerializer(variant)
#                 return Response(serializer.data)
#             except Varient.DoesNotExist:
#                 return Response({"error": "Variant not found"}, status=status.HTTP_404_NOT_FOUND)
#         else:  # If no pk is provided, return all Variants
#             variants = Varient.objects.all()
#             serializer = VariantSerializer(variants, many=True)
#             return Response(serializer.data)  
        

#     def delete(self, request, pk=None):
#         if pk:  # If pk is provided, delete a particular Variant
#             try:                
#                 variant = Varient.objects.get(pk=pk)                
#                 variant.delete()  # Delete the object from the database
#                 return Response({"message": "Variant deleted successfully"}, status=status.HTTP_200_OK)
            
#             except Varient.DoesNotExist:
#                 return Response({"error": "Variant not found"}, status=status.HTTP_404_NOT_FOUND)
          

# views.py

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.exceptions import NotFound
from django.shortcuts import get_object_or_404
from .models import Varient
from .serializers import VariantSerializer


class VariantListCreate(APIView):
    
    def post(self, request):
        """
        Create a new Variant. This method also handles image uploads.
        """
        serializer = VariantSerializer(data=request.data)
        
        if serializer.is_valid():
            # Custom validation to check if the variant can be added
            if not serializer.validated_data.get('add_variant', False):
                return Response(
                    {"error": "This variant cannot be added."},
                    status=status.HTTP_400_BAD_REQUEST
                )

            # Save the variant to the database
            variant = serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        # If validation fails, return the errors
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, pk=None):
        """
        Retrieve a specific Variant or a list of all variants.
        """
        if pk:  # If pk is provided, fetch a particular Variant
            variant = get_object_or_404(Varient, pk=pk)
            serializer = VariantSerializer(variant)
            return Response(serializer.data)
        
        else:  # If no pk is provided, return all Variants
            variants = Varient.objects.all()
            serializer = VariantSerializer(variants, many=True)
            return Response(serializer.data)
    
    def delete(self, request, pk=None):
        """
        Delete a specific Variant.
        """
        if pk:  # If pk is provided, delete a particular Variant
            variant = get_object_or_404(Varient, pk=pk)
            variant.delete()  # Delete the object from the database
            return Response({"message": "Variant deleted successfully"}, status=status.HTTP_200_OK)

        return Response({"error": "No PK provided for deletion"}, status=status.HTTP_400_BAD_REQUEST)
