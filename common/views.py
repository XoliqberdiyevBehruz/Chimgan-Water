from rest_framework import generics

from django_filters.rest_framework import DjangoFilterBackend

from common import models, serializers, filters


class WhyUsListView(generics.ListAPIView):
    queryset = models.WhyUs.objects.all()
    serializer_class = serializers.WhyUsSerializer


class ProductListView(generics.ListAPIView):
    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductSerializer


class MediaListView(generics.ListAPIView):
    queryset = models.Media.objects.all()
    serializer_class = serializers.MediaSerializer


class AboutCompanyListView(generics.ListAPIView):
    queryset = models.AboutCompany.objects.all()
    serializer_class = serializers.AboutCompanySerializer


class FeedbackListView(generics.ListAPIView):
    queryset = models.Feedback.objects.all()
    serializer_class = serializers.FeedbackSerializer


class NewsListView(generics.ListAPIView):
    queryset = models.News.objects.all()
    serializer_class = serializers.NewsSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = filters.NewsFilter


class NewsDetailView(generics.RetrieveAPIView):
    queryset = models.News.objects.all()
    serializer_class = serializers.NewsSerializer
    lookup_field = 'id'


class NewsCategoryListView(generics.ListAPIView):
    queryset = models.NewsCategory.objects.all()
    serializer_class = serializers.NewsCategorySerializer