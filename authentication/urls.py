from django.urls import path, include
from .views import LoginView, LogoutView, SignUpView, upload_photo

urlpatterns = [
    # Auth views
    path('auth/login/',
         LoginView.as_view(), name='auth_login'),

     path('auth/singup/',
         SignUpView.as_view(), name='auth_login'),

    path('auth/logout/',
         LogoutView.as_view(), name='auth_logout'),

    path('/profile/upload_photo', upload_photo, name="upload_photo")
]