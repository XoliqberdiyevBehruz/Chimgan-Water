from django.contrib import admin

from common import models
# Register your models here.

admin.site.register(models.WhyUs)
admin.site.register(models.Product)
admin.site.register(models.Media)
admin.site.register(models.AboutCompany)
admin.site.register(models.Feedback)
admin.site.register(models.NewsCategory)
admin.site.register(models.News)


