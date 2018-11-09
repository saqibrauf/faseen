from django.shortcuts import render
from .models import Location, Store, Circular, Tag, Category


def index(request):
	coupons = Circular.objects.filter(c_type='coupon')
	circulars = Circular.objects.filter(c_type='flyer')
	stores = Store.objects.all()
	context = {
		'coupons' : coupons,
		'stores' : stores,
		'circulars' : circulars,
	}
	return render(request, 'circulars/index.html', context)

def store_detail(request, slug):
	store = Store.objects.get(slug=slug)
	coupons = store.circulars.filter(c_type='coupon')
	circulars = Circular.objects.filter(c_type='flyer')
	context = {
		'store' : store,
		'coupons' : coupons,
		'circulars' : circulars,
	}
	return render(request, 'circulars/store_detail.html', context)