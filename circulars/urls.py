
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('store/<slug>', views.store_detail, name = 'store_detail'),
]
