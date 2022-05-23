from django.contrib import admin
from django.urls import path, include
from account.views import SendPasswordResetEmailView, UserChangePasswrodView, UserRegistrationView, UserLoginView, UserProfileView

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name="register"),
    path('login/', UserLoginView.as_view(), name="login"),
    path('profile/', UserProfileView.as_view(), name="profile"),
    path('changepassword/', UserChangePasswrodView.as_view(), name="changepassword"),
    path('send-reset-password-email/', SendPasswordResetEmailView.as_view(), name="send-reset-password-email"),

]