from django.urls import path
# from .views import CustomObtainTokenPairView#, CustomTokenRefreshView
from rest_framework import routers
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', auth_views.LoginView.as_view(template_name='authentication/login.html'), name='init'),
    path('register/',views.register_view, name='register'),
    path('login/',views.login_view, name='login'),
    path('logout/',views.logout_view, name='logout'),
    path('dashboard/',views.dashboard_view, name='dashboard'),
    # path('token/', CustomObtainTokenPairView.as_view(), name='token_obtain_pair'),
    # path('token/refresh/', CustomTokenRefreshView.as_view(), name='token_refresh'),
]
