from django.urls import path

from .views import homepage, list_posts, post_details, update_post, delete_post, PostListCreateView, PostRetrieveUpdateDeleteView

urlpatterns = [
    path("homepage/", homepage, name="posts_home"),
    path("", PostListCreateView.as_view(), name="list_or_create_post"),
    path("<int:post_id>/", PostRetrieveUpdateDeleteView.as_view(), name="post_details"),
    # path("update/<int:post_id>/", update_post, name="update_post"),
    # path("delete/<int:post_id>/", delete_post, name="delete_post"),
]
