from django.contrib import admin

from .models import Product, ProductImage


class ProductImageline(admin.TabularInline):
    model = ProductImage
    extra = 1



@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImageline]
