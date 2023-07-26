from django.urls import path, include
# from rest_framework import routers
from .views.categories import CategoriesViews, CategoriesEditViews
from .views.subcategories import SubcategoriesViews
from .views.products import ProductsViews
from .views.common import common_views

# router = routers.DefaultRouter()
# router.register(r'terceros',ThirdPartiesViews, 'terceros')

urlpatterns = [
   path("categorias/", CategoriesViews.as_view(), name="categories"),
   path("categorias/<int_pk>", CategoriesEditViews.as_view(), name="categories"),
   # path("categorias/buscar", CategoriesViews.as_view(), name="categories"),
   path("subcategories/", SubcategoriesViews.as_view(), name="subcategories"),
   path("products/", ProductsViews.as_view(), name="products"),
   path('load-html/',common_views, name='common_views'),
]