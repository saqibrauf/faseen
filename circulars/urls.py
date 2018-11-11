
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('stores', views.all_stores, name = 'all_stores'),
    path('store/<slug>', views.store_detail, name = 'store_detail'),
    path('flyers', views.all_flyers, name = 'all_flyers'),
    path('flyer/<slug>', views.flyer_detail, name = 'flyer_detail'),
    path('coupons', views.all_coupons, name = 'all_coupons'),
]
