from django.urls import path
from .views import Index, Catalog

urlpatterns = [
    path("", Index.as_view(), name="index"),
    path("catalog/", Catalog.as_view(), name="catalog"),
]