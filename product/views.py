from django.http import Http404
from rest_framework import status
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView

from .models import Product
from .serializers import ProductSerializer


from django_filters.rest_framework import DjangoFilterBackend


class LargeResultsSetPagination(PageNumberPagination):
    page_size = 9
    page_size_query_param = "per_page"


class ProductList(ListAPIView):
    pagination_class = LargeResultsSetPagination
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["name", "brand", "category__name", "subcategory__name", "slug"]


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
