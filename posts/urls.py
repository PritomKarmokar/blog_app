from django.urls import path

from .views import homepage, list_posts, post_details

urlpatterns = [
    path("homepage/", homepage, name="posts_home"),
    path("", list_posts, name="list_posts"),
    path("<int:post_id>/", post_details, name="post_details"),
]
