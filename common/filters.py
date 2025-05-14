from django.db.models import Q

import django_filters

from common import models

class NewsFilter(django_filters.FilterSet):
    search = django_filters.CharFilter(method='filter_by_search')

    class Meta:
        model = models.News
        fields = ['category', 'search']
    
    def filter_by_search(self, queryset, name, value):
        return queryset.filter(Q(title__icontains=value) | Q(description__icontains=value))