from django.shortcuts import render
from .serializers import ProductSerializer
from .models import Product, ProductImage
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.http import Http404


class ProductList(APIView):
    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

# ID
# class ProductDetail(APIView):
#     def get_object(self, product_id):
#         try:
#             return Product.objects.get(id=product_id)
#         except Product.DoesNotExist:
#             raise Http404
#
#     def get(self, request, product_id):
#         product = self.get_object(product_id)
#         serializer = ProductSerializer(product, many=False)
#         return Response(serializer.data, status.HTTP_200_OK)


# SLUG
class ProductDetail(APIView):
    def get_object(self, slug_text):
        try:
            return Product.objects.get(slug = slug_text)
        except Product.DoesNotExist:
            raise Http404

    def get(self, request, slug_text):
        product = self.get_object(slug_text)
        serializer = ProductSerializer(product, many=False)
        return Response(serializer.data, status.HTTP_200_OK)
