from django.urls import path

from .views import homepage, list_posts, post_details, update_post, delete_post

urlpatterns = [
    path("homepage/", homepage, name="posts_home"),
    path("", list_posts, name="list_posts"),
    path("<int:post_id>/", post_details, name="post_details"),
    path("update/<int:post_id>/", update_post, name="update_post"),
    path("delete/<int:post_id>/", delete_post, name="delete_post"),
]
