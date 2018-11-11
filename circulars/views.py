from django.shortcuts import render
from .models import Location, Store, Flyer, Coupon, Product, Tag, Category


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


#Store Related Views#######################################################################
def all_stores(request):
	stores = Store.objects.all()
	context = {
		'stores' : stores,
	}
	return render(request, 'circulars/all_stores.html', context)

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


#Flyers Related Views#######################################################################
def all_flyers(request):
	flyers = Flyer.objects.all()
	context = {
		'flyers' : flyers,
	}
	return render(request, 'circulars/all_flyers.html', context)

def flyer_detail(request, slug):
	flyer = Flyer.objects.get(slug=slug)
	products = flyer.products.all()
	context = {
		'flyer' : flyer,
		'products' : products,
	}
	return render(request, 'circulars/flyer_detail.html', context)

#Coupon Related Views#######################################################################
def all_coupons(request):
	coupons = Coupon.objects.all()
	context = {
		'coupons' : coupons,
	}
	return render(request, 'circulars/all_coupons.html', context)