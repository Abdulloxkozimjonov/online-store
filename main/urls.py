from django.urls import path
from .views import *

urlpatterns = [
    # ---------------------------------- Start get url -------------------------------------
    path('get-brend/',get_brend),
    path('get-color/',get_color),
    path('get-office/',get_office),
    path('get-category/',get_category),
    path('get-sub_category/',get_sub_category),
    # --------------------------------- Edn get url ----------------------------------

    # --------------------------------- Start filter url -----------------------------

    path('get-sub_category_by_category/<int:pk>/',sub_category_by_category),
    path('get-product-by-price/',product_sale),
    path('get-product_by_rating/',product_by_rating),
    path('get-card-by-user/',card_by_user),
    path('get-brand-by-name/<int:pk>/',brand_by_name),
    path('get-saved_by_user/',saved_by_user),
    path('product_by_brand/<int:pk>/',product_by_brand),
    path('order_by_user/',order_by_user),
    path('product_by_user/',product_by_user),
]