from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='ShopHome'),

    path('about', views.about, name='AboutUs'),
    path('tracker', views.tracker, name='Tracker'),
    path('contact', views.contact, name='ContactUs'),
    path('search', views.search, name='SearchUs'),
    path('productview/<int:myid>', views.productview, name='Product View'),
]