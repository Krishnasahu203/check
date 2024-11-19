
from .models import Product
from rest_framework.views import APIView
from rest_framework.response import Response
from.serializers import ProductSerializer
# Create your views here.


class ProductList(APIView):
    def get(self, request):
        print("GET request received") 
        queryset = Product.objects.all()
        if queryset:
            print("Queryset:", queryset)
        else:
            print("Queryset is empty")
        serializer = ProductSerializer(queryset, many=True)
        if serializer:
            return Response(serializer.data)
        else:
            return Response(serializer.errors)