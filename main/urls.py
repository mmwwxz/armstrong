from django.urls import path
from . import views
from django.shortcuts import redirect


urlpatterns = [
    path('', views.index, name='index'),
    path('catalog/', views.catalog, name='catalog'),
    path('blog/', views.blog, name='blog'),
    path('contact/', views.contact, name='contact'),
    path('detail/<int:product_id>/', views.detail, name='detail'),
    path('detail-blog/<int:blog_id>/', views.detail_blog, name='detail-blog'),
]