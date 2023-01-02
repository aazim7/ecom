from django.contrib import admin
from django.contrib.admin.options import ModelAdmin, TabularInline
from .models import (Category,Product,ProductImage, Cart, AttributeType, AttributeValue, Attribute)


class ImageGallery(TabularInline):
    model = ProductImage    
class VariationsList(TabularInline):
    model = Attribute

@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    inlines = (ImageGallery,VariationsList)
    list_display = ['product_name', 'quantity', 'slug','category', 'price','product_description', 'ptype']

@admin.register(ProductImage)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ['imag_n', 'product','image']

@admin.register(Category)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ['category_name','slug', 'category_image']

@admin.register(Cart)
class CartModelAdmin(admin.ModelAdmin):
    list_display = ['product', 'customer', 'quantity', 'created_at']

@admin.register(AttributeType)
class Atrb(admin.ModelAdmin):
    list_display=["name", "description"]

@admin.register(AttributeValue)
class Avalue(admin.ModelAdmin):
    list_display=["value"]
