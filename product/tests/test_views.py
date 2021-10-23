from django.test import TestCase
from rest_framework.reverse import reverse
from rest_framework.test import APIClient

from product.models import SubCategory, Category, Product


class TestProductAPIView(TestCase):
    def setUp(self):
        self.client = APIClient()
        print(self.client, "self.client")

        self.sub_category1 = SubCategory.objects.create(name="Shirt")
        self.sub_category2 = SubCategory.objects.create(name="T-Shirt")

        self.category = Category.objects.create(name="Men")
        self.category.subcategory.add(self.sub_category1)
        self.category.save()

        self.product = Product.objects.create(
            name="levis Blue Tshirt",
            actual_price=999,
            brand="Levis",
            description="Sizes available - Small, Medium, Large",
        )

        self.product.category.add(self.category)
        self.product.subcategory.add(self.sub_category2)
        self.product.save()

    def test_product_detail_works(self):
        slug = self.product.slug
        url = reverse("product", kwargs={"slug_text": slug})
        response = self.client.get(url)

        assert response.json() != None
        assert response.status_code == 200
        assert response.json()["name"] == self.product.name

        assert (
                response.json()["category"][0]["name"]
                == self.product.category.all().last().name
        )
        assert (
                response.json()["subcategory"][0]["name"]
                == self.product.subcategory.all().last().name
        )

    def test_product_detail_failure(self):
        slug = "vfgjkgykjp9z"
        url = reverse("product", kwargs={"slug_text": slug})
        response = self.client.get(url)
        assert response.status_code == 404
