from django.urls import path, include
from .views import CustomUserView, LoginView, LogoutView, SignUpView, UploadFileAndJson, UserProfileView, upload_photo

from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register("user", CustomUserView)
router.register("user-profile", UserProfileView)

urlpatterns = [
    path("", include(router.urls)),
    # Auth views
    path('auth/login/',
         LoginView.as_view(), name='auth_login'),

     path('auth/singup/',
         SignUpView.as_view(), name='auth_login'),

    path('auth/logout/',
         LogoutView.as_view(), name='auth_logout'),

    path('profile/upload_photo', upload_photo, name="upload_photo"),
    #path('upload', UploadFileAndJson.as_view(), name="upload"),
    #path('upload/', ProfileView.as_view(), name='upload'),
]