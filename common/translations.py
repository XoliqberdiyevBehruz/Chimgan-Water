from modeltranslation.translator import register, TranslationOptions

from common import models 


@register(models.WhyUs)
class WhyUsTranslation(TranslationOptions):
    fields = ('title', 'description')


@register(models.Product)
class ProductTranslation(TranslationOptions):
    fields = ('name', 'description')


@register(models.Feedback)
class FeedbackTranslation(TranslationOptions):
    fields = ('position', 'comment')


@register(models.NewsCategory)
class NewsCategoryTranslation(TranslationOptions):
    fields = ('name',)


@register(models.News)
class NewsTranslation(TranslationOptions):
    fields = ('title', 'description',)