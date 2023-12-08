from django.urls import path
from .views import *

urlpatterns = [
    #------------------------------ Start account url --------------------------------------

    path('sing_up/', singin_view ),
    path('sing_in/', singin_view),
    path('update_user/<int:pk>/', edit_user),
    path('log_uot/', logoout)

    #----------------------------- End account url -----------------------------------------
]