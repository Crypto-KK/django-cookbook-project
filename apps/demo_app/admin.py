from django.contrib import admin

from .models import Idea, Category


admin.site.register(Idea)
admin.site.register(Category)