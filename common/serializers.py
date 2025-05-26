from rest_framework import serializers

from common import models 


class WhyUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.WhyUs
        fields = (
            "id", 'icon', 'title_uz', 'title_ru', 'title_en', 'description_uz', 'description_ru', 'description_en'
        )


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Product
        fields = (
            "id", 'image', 'name_uz', 'name_ru', 'name_en', 'description_uz', 'description_ru', 'description_en'
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
            "id", 'profile_image', 'full_name', 'position_uz', 'position_ru', 'position_en', 'comment_uz', 'comment_ru', 'comment_en', 'rating'
        )


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.News
        fields = (
            "id", 'title_uz', 'title_ru', 'title_en',  'description_uz', 'description_ru', 'description_en', 'image', 
        )


class NewsCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.NewsCategory
        fields = (
            "id", 'name_uz', 'name_ru', 'name_en'
        )
