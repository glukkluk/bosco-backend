from django.urls import path

from app import views

urlpatterns = [
    path("products/", views.products, name="products"),
    path("add_product/", views.add_product, name="add_product"),
    path("replenish/<int:count>", views.replenish, name="replenish"),
]
