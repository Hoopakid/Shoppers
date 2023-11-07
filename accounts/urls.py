from django.urls import path
from accounts.views import *
from django.contrib.auth.views import (
    PasswordResetView,
    PasswordResetDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView
)

urlpatterns = [
    path('login', LoginView.as_view(), name='sign_in'),
    path('register', RegisterView.as_view(), name='sign_up'),
    path('logout', LogoutView.as_view(), name='sign_out'),
    path(
        'reset-password', PasswordResetView.as_view(),
        name='reset_password'
    ),
    path(
        'reset-password-done', PasswordResetDoneView.as_view(),
        name='password_reset_done'
    ),
    path(
        'reset-password/<uidb64>/<token>', PasswordResetConfirmView.as_view(),
        name='password_reset_confirm'
    ),
    path(
        'reset-password-complete', PasswordResetCompleteView.as_view(),
        name='password_reset_complete'
    ),
]
