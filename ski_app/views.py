from django.shortcuts import render, get_object_or_404
from .models import Articles
from django.http import JsonResponse

def articles(request):
    all_articles = Articles.objects.all().order_by("date")
    data = list(all_articles.values())
    return JsonResponse(data, safe=False)


def article(request, id):
    try:
        article_id = int(id)
    except ValueError:
        return JsonResponse(
            {"error": "Invalid article ID"},
            status = 400 )


    article = get_object_or_404(Articles, id=article_id)
    data = {
        "id": article.id,
        "title": article.title,
        "content": article.content,
        "author": article.author.user_name,
        "date": article.date
    }
    return JsonResponse(data)

