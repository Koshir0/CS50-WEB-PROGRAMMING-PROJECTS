
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("indexcopy", views.indexcopy, name="indexcopy"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("new_post", views.new_post, name="new_post"),
    path("edit/<int:postid>", views.edit, name="edit"),
    path("profile/<str:user_id>", views.profile, name="profile"),
    path("followers/<str:user_id>", views.followers, name="followers"),
    path("follow/<str:user_id>", views.follow, name="follow"),
    path("unfollow/<str:user_id>", views.unfollow, name="unfollow"),
    path("following/<int:user_id>", views.following, name="following"),
    path("likes/<int:postid>", views.likes, name="likes"),
    path("unlike/<int:postid>", views.unlike, name="unlike")    
]
