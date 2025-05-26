from django.db.models import Q

import django_filters

from common import models

class NewsFilter(django_filters.FilterSet):
    search = django_filters.CharFilter(method='filter_by_search')

    class Meta:
        model = models.News
        fields = ['category', 'search']
    
    def filter_by_search(self, queryset, name, value):
        return queryset.filter(
            Q(title_uz__icontains=value) |
            Q(title_ru__icontains=value) |
            Q(title_en__icontains=value) |
            Q(description_uz__icontains=value) |
            Q(description_ru__icontains=value) | 
            Q(description_en__icontains=value) 
        )
    