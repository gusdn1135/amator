"""amator URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from page import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.login, name='login'),
    path('home/', views.home, name='home'),
    path('community_notice', views.community_notice, name='community_notice'),
    path('team/', views.team, name='team'),
    path('team_src/', views.team_src, name='team_src'),
    path('community_notice', views.community_notice, name='community_notice'),
    path('community_pr', views.community_pr, name='community_pr'),
    path('community_chat', views.community_chat, name='community_chat'),
    path('notice/<int:notice_id>', views.community_notice_detail, name='community_notice_detail'),
    path('signup_agreement/', views.signup_agreement, name = 'signup_agreement'),
    path('signup_type/', views.signup_type, name = 'signup_type'),
    path('signup_indiv/', views.signup_indiv, name = 'signup_indiv'),
    path('signup_team/', views.signup_team, name = 'signup_team'), 
    path('league_temp/',views.league_temp, name='league_temp'),
    path('league/',views.league, name='league'),
    path('league_detail/', views.league_detail, name='league_detail'),
]
