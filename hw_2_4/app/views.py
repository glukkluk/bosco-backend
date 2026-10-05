import json
from random import choices

from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from app import models


def products(request: HttpRequest) -> HttpResponse:
    all_products = models.Product.objects.all()

    return render(request, "app/products.html", {"products": all_products})


def replenish(request: HttpRequest, count: int) -> HttpResponse:
    with open("app/fixtures/products.json") as f:
        rand_products = choices(json.load(f), k=count)

        for product in rand_products:
            models.Product.objects.create(**product["fields"])

    return HttpResponse(
        f"<h1>Додано {count} нових записів</h1>"
        f"<a href='/products/'><button>Повернутися до списку</button></a>"
    )
