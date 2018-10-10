from django.contrib import admin
from .models import Country, City, Area

class CountryAdmin(admin.ModelAdmin):
    search_fields = ['country']

class CityAdmin(admin.ModelAdmin):
    autocomplete_fields = ['country']
    list_display = ('city', 'country')
    search_fields = ['city']


class AreaAdmin(admin.ModelAdmin):
    prepopulated_fields = {'area_slug': ('area',)}
    autocomplete_fields = ['city']
    search_fields = ['city']
    list_display = ('area', 'city')


admin.site.register(Country, CountryAdmin)
admin.site.register(City, CityAdmin)
admin.site.register(Area, AreaAdmin)