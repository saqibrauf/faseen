from django.contrib import admin
from mptt.admin import MPTTModelAdmin
from .models import Location, Store, Coupon, Tag, Category

class LocationAdmin(MPTTModelAdmin):
    autocomplete_fields = ['parent']
    search_fields = ['name']

class StoreAdmin(admin.ModelAdmin):
	autocomplete_fields = ['location']
	search_fields = ['name']
	list_display = ('name', 'logo')


class CouponAdmin(admin.ModelAdmin):
    autocomplete_fields = ['store', 'tags', 'category']
    list_display = ('product', 'price', 'sale_price', 'store')

class TagAdmin(admin.ModelAdmin):
    search_fields = ['tag']

class CategoryAdmin(MPTTModelAdmin):
    autocomplete_fields = ['parent']
    search_fields = ['name']
    list_display = ('name', 'parent')

admin.site.register(Location, LocationAdmin)
admin.site.register(Store, StoreAdmin)
admin.site.register(Coupon, CouponAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Category, CategoryAdmin)