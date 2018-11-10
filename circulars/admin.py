from django.contrib import admin
from mptt.admin import MPTTModelAdmin
from .models import Location, Store, Tag, Category, Flyer, Coupon, Product

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
class FlyerInline(admin.TabularInline):
    model = Product
    extra = 1
    ordering = ['name']
    show_change_link = True
    exclude = ['coupon']
    autocomplete_fields = ['flyer', 'tags', 'categories']

class FlyerAdmin(admin.ModelAdmin):
    autocomplete_fields = ['store']
    list_display = ('title', 'date_expired', 'store')
    list_select_related = ('store',)
    search_fields = ['title']
    inlines = [
        FlyerInline,
    ]
###############################################################################
class CouponInline(admin.StackedInline):
    model = Product
    extra = 1
    max_num = 1
    ordering = ['name']
    show_change_link = True
    exclude = ['flyer']
    autocomplete_fields = ['tags', 'categories']

class CouponAdmin(admin.ModelAdmin):
    autocomplete_fields = ['store']
    list_display = ('product','date_expired', 'store')
    list_select_related = ('store',)
    search_fields = ['store']
    inlines = [
        CouponInline,
    ]
###############################################################################

class ProductAdmin(admin.ModelAdmin):
    autocomplete_fields = ['flyer', 'tags', 'categories']
    list_display = ('name', 'r_price', 's_price', 'flyer')
    list_select_related = ('flyer',)


admin.site.register(Location, LocationAdmin)
admin.site.register(Store, StoreAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Flyer, FlyerAdmin)
admin.site.register(Coupon, CouponAdmin)
#admin.site.register(Product, ProductAdmin)