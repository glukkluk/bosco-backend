import json
from random import choices

from django.http import HttpRequest, HttpResponse

from app import models


def products(request: HttpRequest) -> HttpResponse:
    all_products = models.Product.objects.all()

    html_table = """<table>
        <tr>
            <th>ID</th>
            <th>Name</th>
            <th>Age category</th>
            <th>Material</th>
            <th>Brand</th>
            <th>Price</th>
        </tr>
    """

    for product in all_products:
        html_table += f"""
        <tr>
            <td>{product.id}</td>
            <td>{product.name}</td>
            <td>{product.age_category}</td>
            <td>{product.material}</td>
            <td>{product.brand}</td>
            <td>{product.price}</td>
        </tr>
        """

    html_table += """</table>"""

    return HttpResponse(html_table)


def replenish(request: HttpRequest, count: int) -> HttpResponse:
    with open("app/fixtures/products.json") as f:
        rand_products = choices(json.load(f), k=count)

        for product in rand_products:
            models.Product.objects.create(**product["fields"])

    return HttpResponse(
        f"<h1>Додано {count} нових записів</h1>"
        f"<a href='/products/'><button>Повернутися до списку</button></a>"
    )
