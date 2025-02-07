from django.contrib import admin

# Register your models here.
from django.contrib import admin

from PlantWebsite.models import Product, Order
admin.site.site_header = "Plant Admin"



class ProductAdmin(admin.ModelAdmin):
    def change_category_to_default(self,request,queryset):
        self.change_category_to_default.short_description = 'Default Category'
    list_display = ('title','price','discount_price','category','description','image')






admin.site.register(Product,ProductAdmin)
admin.site.register(Order)