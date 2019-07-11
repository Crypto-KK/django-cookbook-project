from django.contrib import admin
from django.template.loader import render_to_string
from django.utils.text import mark_safe

from .models import Product, ProductPhoto


class ProductPhotoInline(admin.StackedInline):
    model = ProductPhoto
    extra = 0


class ProductAdmin(admin.ModelAdmin):
    list_display = ['get_photo', 'title', 'price']
    list_display_links = ['title',]
    list_editable = ['price']

    fieldsets = (
        '产品', {
            'fields': ('title', 'slug', 'desc', 'price')
        }
    )
