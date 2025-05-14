from django.urls import path

from common import views 

urlpatterns = [
    path('why-us/list/', views.WhyUsListView.as_view(), name='why-us'),
    path('product/list/', views.ProductListView.as_view(), name='products'),
    path('media/list/', views.MediaListView.as_view(), name='media'),
    path('about-company/', views.AboutCompanyListView.as_view(), name='about-company'),
    path('feedback/list/', views.FeedbackListView.as_view(), name='feedback'),
    path('news/list/', views.NewsListView.as_view(), name='news'),
    path('news/<int:id>/', views.NewsListView.as_view(), name='news-detail'),
    path('news/category/list/', views.NewsCategoryListView.as_view(), name='news-category'),
]