from django.shortcuts import render
from .models import Location, Store, Flyer,Coupon, Product, Tag, Category


def index(request):
	stores = Store.objects.all()
	coupons = Coupon.objects.all()
	flyers = Flyer.objects.all()
	context = {
		'stores' : stores,
		'coupons' : coupons,
		'flyers' : flyers,
	}
	return render(request, 'circulars/index.html', context)

def store_detail(request, slug):
	store = Store.objects.get(slug=slug)
	coupons = store.coupons.all()
	flyers = store.flyers.all()
	context = {
		'store' : store,
		'coupons' : coupons,
		'flyers' : flyers,
	}
	return render(request, 'circulars/store_detail.html', context)