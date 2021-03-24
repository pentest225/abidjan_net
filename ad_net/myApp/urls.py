from django.contrib import admin
from django.urls import path ,include
from .import views

urlpatterns = [
    path('', views.index),
    path('getAllArticles',views.getArticle),
    path('addArticle',views.addArticle)
]