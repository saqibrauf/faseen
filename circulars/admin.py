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
    def products(self, obj):
        count = Product.objects.filter(flyer=obj.id).count()
        return count
    autocomplete_fields = ['store']
    list_display = ('title', 'products','date_expired', 'store')
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
    def price(self, obj):
        product = Product.objects.get(coupon=obj.id)
        regular_price = product.r_price
        sale_price = product.s_price
        return str(regular_price) + ' --> ' + str(sale_price)

    autocomplete_fields = ['store']
    list_display = ('products', 'price', 'date_expired', 'store')
    list_select_related = ('store',)
    search_fields = ['store']
    inlines = [
        CouponInline,
    ]
###############################################################################

class ProductAdmin(admin.ModelAdmin):
    def related_to(self, obj):
        if obj.flyer:
            related = obj.flyer.title
        else:
            related = 'Coupon --> ' + obj.name
        return related

    autocomplete_fields = ['flyer', 'tags', 'categories']
    list_display = ('name', 'r_price', 's_price', 'related_to')
    #list_select_related = ('flyer', 'coupon')


admin.site.register(Location, LocationAdmin)
admin.site.register(Store, StoreAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Flyer, FlyerAdmin)
admin.site.register(Coupon, CouponAdmin)
admin.site.register(Product, ProductAdmin)