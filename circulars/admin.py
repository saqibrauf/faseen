from django.contrib import admin
from mptt.admin import MPTTModelAdmin
from .models import Location, Store, Tag, Category, Circular, Product

class LocationAdmin(MPTTModelAdmin):
    autocomplete_fields = ['parent']
    search_fields = ['name']

class StoreAdmin(admin.ModelAdmin):
	autocomplete_fields = ['location']
	search_fields = ['name']
	list_display = ('name', 'logo')

class TagAdmin(admin.ModelAdmin):
    search_fields = ['tag']

class CategoryAdmin(MPTTModelAdmin):
    autocomplete_fields = ['parent']
    search_fields = ['name']
    list_display = ('name', 'parent')

##############################################################################
class CircularInline(admin.TabularInline):
    model = Product
    extra = 1
    ordering = ['name']
    show_change_link = True
    autocomplete_fields = ['circular', 'tags', 'categories']

class CircularAdmin(admin.ModelAdmin):
    autocomplete_fields = ['store']
    list_display = ('title', 'c_type', 'date_expired', 'store')
    list_select_related = ('store',)
    search_fields = ['title']
    inlines = [
        CircularInline,
    ]
###############################################################################

class ProductAdmin(admin.ModelAdmin):
    autocomplete_fields = ['circular', 'tags', 'categories']
    list_display = ('name', 'r_price', 's_price', 'circular')
    list_select_related = ('circular',)


admin.site.register(Location, LocationAdmin)
admin.site.register(Store, StoreAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Circular, CircularAdmin)
#admin.site.register(Product, ProductAdmin)