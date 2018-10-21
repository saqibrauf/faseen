from django.contrib import admin
from .models import Country, City, Store, Coupon, Tag, Category

class CountryAdmin(admin.ModelAdmin):
    search_fields = ['country']

class CityAdmin(admin.ModelAdmin):
    autocomplete_fields = ['country']
    list_display = ('city', 'country')
    search_fields = ['city']


class StoreAdmin(admin.ModelAdmin):
	autocomplete_fields = ['city']
	search_fields = ['store']
	list_display = ('store', 'store_logo')


class CouponAdmin(admin.ModelAdmin):
    autocomplete_fields = ['store', 'tags', 'category']
    list_display = ('product', 'price', 'sale_price', 'store')

class TagAdmin(admin.ModelAdmin):
    search_fields = ['tag']

class CategoryAdmin(admin.ModelAdmin):
    autocomplete_fields = ['parent']
    search_fields = ['cat']
    list_display = ('cat', 'parent')

admin.site.register(Country, CountryAdmin)
admin.site.register(City, CityAdmin)
admin.site.register(Store, StoreAdmin)
admin.site.register(Coupon, CouponAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Category, CategoryAdmin)