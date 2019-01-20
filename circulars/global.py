from .models import Store, Category, Location

def global_var(request):
	STORES_MENU = Store.objects.all()
	CATEGORIES = Category.objects.filter(parent=None).order_by('name')
	LOCATIONS = Location.objects.all()
	return {
		'STORES_MENU' : STORES_MENU,
		'CATEGORIES' : CATEGORIES,
		'LOCATIONS' : LOCATIONS,
	}