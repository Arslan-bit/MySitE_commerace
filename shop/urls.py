from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='ShopHome'),
    path('about', views.index, name='AboutUs'),

]
