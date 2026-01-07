from django.shortcuts import render, get_object_or_404
from .models import User, Ranking, Tag, Articles, ArticlesComments, Video, VideoComments, Slopes
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import UserSerializer, RankingSerializer


@api_view(['GET'])
def usersList(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def rankingList(request):
    ranking = Ranking.objects.all()
    serializer = RankingSerializer(ranking, many=True)
    return Response(serializer.data)