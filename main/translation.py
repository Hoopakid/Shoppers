from modeltranslation.translator import TranslationOptions, translator
from .models import *


class ProductTranslation(TranslationOptions):
    fields = ('name', 'description')


translator.register(Product, ProductTranslation)
