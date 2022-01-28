from re import template
from django.urls import path, include
from .views import CreatePro, ProfileView, UserReg, Upd_Pro, PassWord, EditProfileView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/', UserReg.as_view(), name='register'),
    path('profile_edit/', Upd_Pro.as_view(), name='edit_pro'),
    path('password/', PassWord.as_view(template_name='registration/change-password.html')),
    path('<int:pk>/profile', ProfileView.as_view(), name='userprofile'),
    path('<int:pk>/profile_page_edit',
         EditProfileView.as_view(), name='edituserprofile'),
    path('create_profile_page_edit', CreatePro.as_view(), name='createuserprofile'),
]
