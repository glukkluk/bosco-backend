import json
from random import choices

from django.contrib import messages
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render

from app import models


def products(request: HttpRequest) -> HttpResponse:
    all_products = models.Product.objects.all()

    return render(request, "app/products.html", {"products": all_products})


def add_product(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        print(request.POST)
        name = request.POST.get("name")
        age_category = request.POST.get("age_category")
        material = request.POST.get("material")
        brand = request.POST.get("brand")
        price = request.POST.get("price")

        models.Product.objects.create(
            name=name,
            age_category=age_category,
            material=material,
            brand=brand,
            price=price,
        )
        messages.success(request, "Product added successfully")
        return redirect("products")

    return render(request, "app/add_product.html")


def replenish(request: HttpRequest, count: int) -> HttpResponse:
    with open("app/fixtures/products.json") as f:
        rand_products = choices(json.load(f), k=count)

        for product in rand_products:
            models.Product.objects.create(**product["fields"])

    return HttpResponse(
        f"<h1>Додано {count} нових записів</h1>"
        f"<a href='/products/'><button>Повернутися до списку</button></a>"
    )
