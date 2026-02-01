from modeltranslation.translator import register, TranslationOptions
from .models import News, Category

@register(News)
class NewsTranslationOptions(TranslationOptions):
    fields = ('title', 'body', 'author')
    
@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('name',)
