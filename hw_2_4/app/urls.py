from django.urls import path

from app import views

urlpatterns = [
    path("products/", views.products),
    path("replenish/<int:count>", views.replenish),
]
