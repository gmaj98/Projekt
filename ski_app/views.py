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
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.decorators import api_view, permission_classes


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticatedOrReadOnly])
def users_list(request):
    if request.method == 'GET':
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticatedOrReadOnly])
def ranking_list(request):
    if request.method == 'GET':
        ranking = Ranking.objects.all()
        serializer = RankingSerializer(ranking, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = RankingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticatedOrReadOnly])
def tags_list(request):
    if request.method == 'GET':
        tags = Tag.objects.all()
        serializer = TagSerializer(tags, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = TagSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticatedOrReadOnly])
def articles_list(request):
    if request.method == 'GET':
        articles = Articles.objects.all().order_by('-date')
        serializer = ArticlesSerializer(articles, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ArticlesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


@api_view(['GET'])
def article_detail(request, pk):
    article = get_object_or_404(Articles, pk=pk)
    serializer = ArticlesSerializer(article)
    return Response(serializer.data)


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticatedOrReadOnly])
def article_comments_list(request, article_id):
    if request.method == 'GET':
        comments = ArticlesComments.objects.filter(article_id=article_id)
        serializer = ArticlesCommentsSerializer(comments, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ArticlesCommentsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticatedOrReadOnly])
def videos_list(request):
    if request.method == 'GET':
        videos = Video.objects.all().order_by('-date')
        serializer = VideoSerializer(videos, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = VideoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


@api_view(['GET'])
def video_detail(request, pk):
    video = get_object_or_404(Video, pk=pk)
    serializer = VideoSerializer(video)
    return Response(serializer.data)


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticatedOrReadOnly])
def video_comments_list(request, video_id):
    if request.method == 'GET':
        comments = VideoComments.objects.filter(video_id=video_id)
        serializer = VideoCommentsSerializer(comments, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = VideoCommentsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticatedOrReadOnly])
def slopes_list(request):
    if request.method == 'GET':
        slopes = Slopes.objects.all()
        serializer = SlopesSerializer(slopes, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = SlopesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)