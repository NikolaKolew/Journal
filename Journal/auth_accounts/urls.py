from django.contrib.auth.views import LogoutView
from django.urls import path

from Journal.auth_accounts.views import CustomLoginView, RegisterPage, ProfileDetail, ProfileUpdate, DashboardStaff, \
    BanUpdate, UserChangePassword

urlpatterns = (
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='index'), name='logout'),
    path('register/', RegisterPage.as_view(), name='register'),
    path('change-password/', UserChangePassword.as_view(), name='change-password'),
    path('profile/', ProfileDetail.as_view(), name='profile-page'),
    path('profile/edit/<int:pk>', ProfileUpdate.as_view(), name='profile-update'),
    path('dashboard/', DashboardStaff.as_view(), name='dashboard'),
    path('ban/<int:pk>/', BanUpdate.as_view(), name='ban-update'),
)

import Journal.auth_accounts.signals