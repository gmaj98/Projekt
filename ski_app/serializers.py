from rest_framework import serializers
from .models import User, Ranking, Tag, Articles, ArticlesComments, Video, VideoComments, Slopes

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "email", "user_name", "first_name")


class RankingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ranking
        fields = '__all__'


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'


class ArticlesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Articles
        fields = '__all__'


class ArticlesCommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArticlesComments
        fields = '__all__'


class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = '__all__'


class VideoCommentsSerialzier(serializers.ModelSerializer):
    class Meta:
        model = VideoComments
        fields = '__all__'


class SlopesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Slopes
        fields = '__all__'
