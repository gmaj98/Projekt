from rest_framework import serializers
from .models import User, Ranking, Tag, Articles, ArticlesComments, Video, VideoComments, Slopes

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class RankingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ranking
        fields = '__all__'

        