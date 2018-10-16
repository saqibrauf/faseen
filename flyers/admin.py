from django.contrib import admin
from .models import Country, City, Area, Store, Coupon, Tag

class CountryAdmin(admin.ModelAdmin):
    search_fields = ['country']

class CityAdmin(admin.ModelAdmin):
    autocomplete_fields = ['country']
    list_display = ('city', 'country')
    search_fields = ['city']


class AreaAdmin(admin.ModelAdmin):
    autocomplete_fields = ['city']
    search_fields = ['city']
    list_display = ('area', 'city')


class StoreAdmin(admin.ModelAdmin):
	autocomplete_fields = ['city', 'area']
	search_fields = ['store']
	list_display = ('store', 'store_logo')


class CouponAdmin(admin.ModelAdmin):
    autocomplete_fields = ['store', 'tags']

class TagAdmin(admin.ModelAdmin):
    search_fields = ['tag']

admin.site.register(Country, CountryAdmin)
admin.site.register(City, CityAdmin)
admin.site.register(Area, AreaAdmin)
admin.site.register(Store, StoreAdmin)
admin.site.register(Coupon, CouponAdmin)
admin.site.register(Tag, TagAdmin)