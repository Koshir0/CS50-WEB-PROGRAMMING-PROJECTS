from django.urls import path

from . import views



urlpatterns = [
    path("", views.index, name="index"),
    path("<str:title>", views.wiki, name="title"),
    path("wiki/<str:title>", views.wiki, name="entry"),
    path("search/", views.search, name="search"),
    path("create/", views.create, name="create"),
    path("update/<str:title>", views.update_page, name="update_page"),
    path("update/", views.update, name="update"),
    path("randompage/", views.randompage, name="randompage")
]
