from django.contrib import admin

from shop.models import Product, Category


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'category', 'price', 'image', 'description')
    list_display_links = ('name', 'slug')
    list_filter = ('category',)
    search_fields = ('name', 'description', 'category__name')
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'image', 'description')
    list_display_links = ('name', 'slug')
    search_fields = ('name', 'description')
    prepopulated_fields = {'slug': ('name',)}
