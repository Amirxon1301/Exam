from .models import Maqola
from modeltranslation.translator import TranslationOptions, register

@register(Maqola)
class MaqolaTranslationOptions(TranslationOptions):
    fields = ('sarlavha', 'matn', 'mavzu')