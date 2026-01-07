from django.urls import path
from .import views

urlpatterns = [
    #USERS
    path('users/', views.users_list, name='users-list'),

    #RANKING
    path('ranking/', views.ranking_list, name='ranking-list'),

    #TAGS
    path('tags/', views.tags_list, name='tags-list'),

    #ARTICELS
    path('articles/', views.articles_list, name='articles-list'),
    path('articles/<int:pk>/', views.article_detail, name='article-detail'),
    path('articles/<int:article_id>/comments/', views.article_comments_list, name='article-comments-list'),

    #VIDEOS
    path('videos/', views.videos_list, name='videos-list'),
    path('videos/<int:pk>/', views.video_detail, name='video-detail'),
    path('videos/<int:video_id>/comments/', views.video_comments_list, name='video-comments-list'),

    #SLOPES
    path('slopes/', views.slopes_list, name='slopes-list'),
]
