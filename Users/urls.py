from django.conf.urls import include

from django.urls import path
from Users.views import create_user, create_order, success, display_hotel_images, signup
urlpatterns = [
    path('create', create_user),
    path('order', create_order),
    path('success', success, name = 'success'),
    path('hotel_images', display_hotel_images, name = 'hotel_images'),
    path('sign_up', signup)

]