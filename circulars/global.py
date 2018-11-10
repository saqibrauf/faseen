from .models import Store

def global_var(request):
	STORES_MENU = Store.objects.all()
	return {
		'STORES_MENU' : STORES_MENU,
	}