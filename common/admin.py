from django.contrib import admin

from modeltranslation.admin import TranslationAdmin

from common import models
# Register your models here.

admin.site.register(models.WhyUs, TranslationAdmin)
admin.site.register(models.Product, TranslationAdmin)
admin.site.register(models.Media)
admin.site.register(models.AboutCompany)
admin.site.register(models.Feedback, TranslationAdmin)
admin.site.register(models.NewsCategory, TranslationAdmin)
admin.site.register(models.News, TranslationAdmin)


