from django.contrib import admin
from django.urls import path, include

from rest_framework.routers import DefaultRouter

from posts.views import PostViewSet
from accounts.views import SignUpView

router = DefaultRouter()
router.register("", PostViewSet, basename="posts")

urlpatterns = [
    path("admin/", admin.site.urls),
    # path("posts/", include("posts.urls")),
    path("posts/", include(router.urls)),
    path("auth/", include('accounts.urls')),
]
