from django.contrib import admin
from .models import Category, Product


# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Category, CategoryAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'stock', 'avaviable', 'created', 'update']
    list_editable = ['price', 'stock', 'avaviable']
    prepopulated_fields = {'slug': ('name',)}
    list_per_page = 25


admin.site.register(Product, ProductAdmin)
