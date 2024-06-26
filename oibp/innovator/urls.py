"""oibp URL Configuration

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
from django.urls import path, include
from innovator import views

urlpatterns = [
    path('dashboard', views.dashboard, name='dashboard'),
    path('add_idea', views.add_idea, name='add_idea'),
    path('all_idea', views.all_idea, name='all_idea'),
    path('delete_idea/<int:id>', views.delete_idea, name='delete_idea'),
    path('inquiry', views.inquiry, name='inquiry'),
    path('orders', views.orders, name='orders'),
    path('feedback', views.feedback, name='feedback'),
    path('editprofile', views.editprofile, name='editprofile'),
    path('upload_profile_pic', views.upload_profile_pic, name='upload_profile_pic'),
    
]
