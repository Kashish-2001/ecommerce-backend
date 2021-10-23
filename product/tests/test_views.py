from rest_framework.reverse import reverse
from rest_framework.test import APIClient
import pytest
from product.models import SubCategory, Category, Product


@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def detail_view(db):
    sub_category1 = SubCategory.objects.create(name="Shirt")
    sub_category2 = SubCategory.objects.create(name="T-Shirt")

    category = Category.objects.create(name="Men")
    category.subcategory.add(sub_category1)
    category.save()

    product = Product.objects.create(
        name="levis Blue Tshirt",
        actual_price=999,
        brand="Levis",
        description="Sizes available - Small, Medium, Large",
    )

    product.category.add(category)
    product.subcategory.add(sub_category2)
    product.save()
    return product


def test_product_detail_works(api_client, detail_view):
    product = detail_view
    slug = product.slug
    url = reverse("product", kwargs={"slug_text": slug})
    response = api_client.get(url)

    assert response.json() != None
    assert response.status_code == 200
    assert response.json()["name"] == product.name

    assert (
            response.json()["category"][0]["name"]
            == product.category.all().last().name
    )
    assert (
            response.json()["subcategory"][0]["name"]
            == product.subcategory.all().last().name
    )


def test_product_detail_failure(api_client, detail_view):
    slug = "vfgjkgykjp9z"
    url = reverse("product", kwargs={"slug_text": slug})
    response = api_client.get(url)
    assert response.status_code == 404