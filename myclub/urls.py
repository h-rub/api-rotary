# File URLS MyClub App
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CreatePost, GetPosts, SaveReaction, ping

router = DefaultRouter()

# router.register("user", CustomUserView)
# router.register("user-profile", UserProfileView)

urlpatterns = [
    path("", include(router.urls)),
    path("club", ping, name="pong"),

    path("myclub/posts", GetPosts.as_view({'get': 'list'}), name="posts"),
    path("myclub/posts/reaction", SaveReaction.as_view(), name="save_like" ),
    path("myclub/post/create", CreatePost.as_view(), name="create_post")
]