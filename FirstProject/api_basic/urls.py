from django.urls import path
from .views import article_list
from .views import article_detail

urlpatterns = [
    path('article/', article_list),
    path('article_detail/<int:pk>', article_detail)
]