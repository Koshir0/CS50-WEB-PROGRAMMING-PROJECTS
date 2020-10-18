from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("create", views.create, name="create"),
    path("watchlist", views.watchlist, name="watchlist"),
    path("watch/<int:listing_id>", views.watch, name="watch"),
    path("delete/<int:listing_id>", views.delete, name="delete"),
    path("listings/<int:listing_id>", views.listing, name="listing"),
    path("accounts/login/?next=/listings/<int:listing_id>", views.not_allowed, name="not_allowed"),
    path("bid/<int:listing_id>", views.bid, name="bid"),
    path("close/<int:listing_id>", views.close, name="close"),
    path("comment/<int:listing_id>", views.comment, name="comment"),
    path("categories", views.categories, name="categories"),
    path("all_cate/<str:cate>", views.all_cate, name="all_cate")







]
