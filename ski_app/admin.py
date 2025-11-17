from django.contrib import admin
from .models import User, Ranking, Tag, Articles, ArticlesComments, Video, VideoComments, Slopes

# Register your models here.
admin.site.register(User)
admin.site.register(Ranking)
admin.site.register(Tag)
admin.site.register(Articles)
admin.site.register(ArticlesComments)
admin.site.register(Video)
admin.site.register(VideoComments)
admin.site.register(Slopes)

