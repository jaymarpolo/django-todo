from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.registerPage, name='register'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutPage, name='logout'),
    path('update/<int:pk>', views.update, name='update'),
    path('delete/<int:pk>/', views.delete, name='delete'),
    path('reset-password/', auth_views.PasswordResetView.as_view(template_name='registration/reset.html'), name='reset_password'),
    path('reset-password-sent/', auth_views.PasswordResetDoneView.as_view(template_name='registration/reset-sent.html'), name='password_reset_done'),
    path('reset-password<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='registration/reset-confirm.html'), name='password_reset_confirm'),
    path('reset-password-complete/', auth_views.PasswordResetCompleteView.as_view(template_name='registration/reset-complete.html'), name='password_reset_complete'),
]
