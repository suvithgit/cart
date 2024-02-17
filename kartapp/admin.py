from django.contrib import admin
from .models import CATEGORY,PRODUCT

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name','slug']
    prepopulated_fields = {'slug':('name',)}
admin.site.register(CATEGORY,CategoryAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name','price','stock','avilable','create','update']
    list_editable = ['price','stock','avilable']
    prepopulated_fields = {'slug':('name',)}
    list_per_page = 20
admin.site.register(PRODUCT,ProductAdmin)
