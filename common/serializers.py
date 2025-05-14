from rest_framework import serializers

from common import models 


class WhyUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.WhyUs
        fields = (
            "id", 'icon', 'title', 'description'
        )


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Product
        fields = (
            "id", 'image', 'name', 'description'
        )


class MediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Media
        fields = (
            "id", 'image'
        )


class AboutCompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.AboutCompany
        fields = (
            "id", 'expirience', 'clients', 'partners', 'products'
        )


class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Feedback
        fields = (
            "id", 'profile_image', 'full_name', 'position', 'comment', 'rating'
        )


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.News
        fields = (
            "id", 'title', 'description', 'image', 
        )


class NewsCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.NewsCategory
        fields = (
            "id", 'name'
        )
