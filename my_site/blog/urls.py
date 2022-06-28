from urllib.parse import urlparse
from django.urls import path
from . import views


urlpatterns = [
    path("", views.starting_page, name="starting-page"),
    path("posts", views.posts, name="posts-page"),
    path("posts/the-code", views.post_detail, name="post-details"),
    # path("posts/<slug:slug>", views.post_detail, name="post-details"),
]
