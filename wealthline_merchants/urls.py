"""wealthline_merchants URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from home.views import *
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeViews, name='home'),
    path('about-Us/',AboutViews,name="about"),
    path('blog/<blog_title>/',DetailViews,name="detail"),
    path('story/<ragp_stories_name>/', StoryViews, name='story'),
    path('blog/',MoreStoriesViews,name="morestories"),
    path('story/',MorePostsViews,name="moreposts"),
]