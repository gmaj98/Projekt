from django.urls import path
from .import views

urlpatterns = [
    path("users-list/", views.usersList, name="users_list"),
    path("ranking/", views.rankingList, name='ranking')
]
