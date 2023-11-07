from django.contrib import admin
from .models import *
from modeltranslation.admin import TranslationAdmin


@admin.register(Product)
class ProductAdmin(TranslationAdmin):
    pass


admin.site.register((Image, ShoppingCart))
