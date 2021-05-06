from django.http import Http404
from rest_framework import status
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Product
from .serializers import ProductSerializer


class ProductList(APIView):
    def get(self, request):
        products = Product.objects.all()
        total_products = len(Product.objects.all())
        paginator = PageNumberPagination()
        result_page = paginator.paginate_queryset(products, request)
        serializer = ProductSerializer(result_page, many=True)
        return Response({"total_products": total_products, "products": serializer.data}, status=status.HTTP_200_OK)


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
            return Product.objects.get(slug=slug_text)
        except Product.DoesNotExist:
            raise Http404

    def get(self, request, slug_text):
        product = self.get_object(slug_text)
        serializer = ProductSerializer(product, many=False)
        return Response(serializer.data, status.HTTP_200_OK)