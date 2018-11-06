from django.shortcuts import render
from .models import Location, Store, Coupon, Tag, Category


def index(request):
	coupons = Coupon.objects.all()
	stores = Store.objects.all()
	context = {
		'coupons' : coupons,
		'stores' : stores,
	}
	return render(request, 'circulars/index.html', context)