from django.urls import path
from .views import *


urlpatterns = [
    # ---------------------------------- Start order url ----------------------------------------

    path('create-order/', create_order),
    path('edit-order/<int:pk>/', edit_order),
    path('delete-order/<int:pk>/', delete_order),

    # ----------------------------------- End order url -----------------------------------------

    # ----------------------------------- Start adress url --------------------------------------
    path('create-adress/', create_adress),
    path('edit-adress/<int:pk>/', edit_address),
    path('delete-adress/<int:pk>/', delete_address),

    # ----------------------------------- End adress url ----------------------------------------

    # ----------------------------------- Start category url ------------------------------------

    path('create-category/',create_category),
    path('edit-category/<int:pk>/',edit_category),
    path('delete-category/<int:pk>/',delete_category),

    # ----------------------------------- End cotegory url --------------------------------------

    # ----------------------------------- Start sub-catogory url --------------------------------

    path('create-sub-category/',create_sub_category),
    path('edit-sub-category/<int:pk>/',edit__sub_category),
    path('delete-sub-category/<int:pk>/',delete__sub_category),

    # ------------------------------------ End sub-category url ---------------------------------

    # ------------------------------------ Start color url --------------------------------------

    path('create-color/',create_color),
    path('edit-color/<int:pk>/',edit_color),
    path('delete-color/<int:pk>/',delete_color),

    # ------------------------------------ End color url ----------------------------------------

    # ------------------------------------ Start image url --------------------------------------

    path('create-image/',create_image),
    path('edit-image/<int:pk>/',edit_image),
    path('delete-image/<int:pk>/',delete_image),

    # ------------------------------------ End image url ----------------------------------------

    # ------------------------------------ Start size-url ---------------------------------------

    path('create-size-category/', create_size_category),
    path('edit-size-category/<int:pk>/', edit_size_category),
    path('delete-size-category/<int:pk>/', delete_size_category),

    # ------------------------------------ End size url -----------------------------------------

    # ------------------------------------ Start card url ---------------------------------------

    path('create-card/', create_card),
    path('edit-card<int:pk>/', edit_card),
    path('delete-card<int:pk>/', delete_card),

    # ----------------------------------- End card url ------------------------------------------

    # ----------------------------------- Start saved url ---------------------------------------

    path('create-saved/', create_saved),
    path('edit-saved<int:pk>/', edit_saved),
    path('delete-saved<int:pk>/', delete_saved),

    # ---------------------------------- End saved url ------------------------------------------

    # --------------------------------- Start office url ----------------------------------------

    path('create-office/', create_office),
    path('edit-office/<int:pk>/', edit_office),
    path('delete-office/<int:pk>/', delete_office),

    # -------------------------------- End office url ------------------------------------------

# --------------------------------- Start office url ----------------------------------------

    path('create-product/', create_product),
    path('edit-office/<int:pk>/', edit_product),
    path('delete-office/<int:pk>/', delete_product),

    # -------------------------------- End office url ------------------------------------------
]