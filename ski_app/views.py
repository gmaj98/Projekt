from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import (
    User, Ranking, Tag,
    Articles, ArticlesComments,
    Video, VideoComments,
    Slopes
)
from .serializers import (
    UserSerializer, RankingSerializer, TagSerializer,
    ArticlesSerializer, ArticlesCommentsSerializer,
    VideoSerializer, VideoCommentsSerializer,
    SlopesSerializer
)

@api_view(['GET'])
def users_list(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def ranking_list(request):
    ranking = Ranking.objects.all()
    serializer = RankingSerializer(ranking, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def tags_list(request):
    tags = Tag.objects.all()
    serializer = TagSerializer(tags, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def articles_list(request):
    articles = Articles.objects.all().order_by('-date')
    serializer = ArticlesSerializer(articles, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def article_detail(request, pk):
    article = get_object_or_404(Articles, pk=pk)
    serializer = ArticlesSerializer(article)
    return Response(serializer.data)


@api_view(['GET'])
def article_comments_list(request, article_id):
    comments = ArticlesComments.objects.filter(article_id=article_id)
    serializer = ArticlesCommentsSerializer(comments, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def videos_list(request):
    videos = Video.objects.all().order_by('-date')
    serializer = VideoSerializer(videos, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def video_detail(request, pk):
    video = get_object_or_404(Video, pk=pk)
    serializer = VideoSerializer(video)
    return Response(serializer.data)


@api_view(['GET'])
def video_comments_list(request, video_id):
    comments = VideoComments.objects.filter(video_id=video_id)
    serializer = VideoCommentsSerializer(comments, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def slopes_list(request):
    slopes = Slopes.objects.all()
    serializer = SlopesSerializer(slopes, many=True)
    return Response(serializer.data)