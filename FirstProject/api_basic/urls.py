from django.urls import path
# from .views import article_list
# from .views import article_detail
from .views import ArticleAPIViews, ArticleDetail

urlpatterns = [

    path('article/', ArticleAPIViews.as_view()),
    path('article_detail/<int:id>', ArticleDetail.as_view())
]


    # path('article/', article_list),
    # path('article_detail/<int:pk>', article_detail)