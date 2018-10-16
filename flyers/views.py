from django.shortcuts import render
from .models import Country, City, Area, Store, Coupon


def index(request):
	coupons = Coupon.objects.all()
	stores = Store.objects.all()
	context = {
		'coupons' : coupons,
		'stores' : stores,
	}
	return render(request, 'flyers/index.html', context)