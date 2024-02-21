from . import views
from django.urls import path
from django.contrib.auth import views as auth_views
app_name = 'users'
urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register, name='register'),
    path("<int:pk>", views.update, name="update"),
    path("updaterecord/<int:pk>", views.updaterecord, name="updaterecord" ),
    path("reset_password/", auth_views.PasswordResetView.as_view(), name="password_reset"),
    path("reset_password_sent/", auth_views.PasswordResetDoneView.as_view(), name="password_reset_done"),
    path("reset/<uidb64>/<token>/", auth_views.PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
    path("reset_password_complete/", auth_views.PasswordResetCompleteView.as_view(), name="password_reset_complete"),
]
