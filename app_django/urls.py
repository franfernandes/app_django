"""app_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from allauth.account.views import LoginView, LogoutView, SignupView, PasswordChangeView
from django.contrib.auth import views as auth_views
from django.contrib import admin
from django.urls import path, include
from . import views



urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', LoginView.as_view(), name='account_login'),
    path('logout/', LogoutView.as_view(), name='account_logout'),
    path('signup/', SignupView.as_view(), name='account_signup'),
    path('accounts/', include('allauth.urls')),
    path('accounts/', include('allauth.socialaccount.urls')),
    path('', auth_views.LoginView.as_view(), name='login'),
    path('accounts/password/set/', views.CustomPasswordSetRedirectView, name='set_password'),
    path('dados/', views.dados, name='dados'),

     
]
