from django.urls import path
from userauths import views

app_name = "userauths"

urlpatterns = [
    path("sign-up/", views.register_view, name="sign-up"), 
    path("sign-in/", views.login_view, name="sign-in"),
    path("sign-out/", views.logout_view, name="sign-out"),
    path("profile/edit/", views.profile_edit, name="profile-edit"),
    path('activate/<uidb64>/<token>', views.activate, name='activate'),
    path("reset-password/", views.reset_password, name="reset-password"),
    path('reset/<uidb64>/<token>', views.passwordResetConfirm, name='reset-password-confirm'),
]