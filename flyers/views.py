from django.shortcuts import render
from .models import Country, City, Store, Coupon, Tag, Category


def index(request):
	coupons = Coupon.objects.all()
	stores = Store.objects.all()
	context = {
		'coupons' : coupons,
		'stores' : stores,
	}
	return render(request, 'flyers/index.html', context)