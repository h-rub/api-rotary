# File URLS polls App
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CreatePost, GetPosts, SaveReaction, ping

router = DefaultRouter()

# router.register("user", CustomUserView)
# router.register("user-profile", UserProfileView)

urlpatterns = [
    path("", include(router.urls)),
    path("polls", ping, name="pong"),

    path("polls/posts", GetPosts.as_view({'get': 'list'}), name="posts"),
    path("polls/vote", SaveReaction.as_view(), name="save_like" ),
    path("polls/create", CreatePost.as_view(), name="create_post")
]