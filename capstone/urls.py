"""capstone URL Configuration

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
from django.urls import path, re_path
from removals import views
from django.views.static import serve
from . import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="index"),
    path('login', views.login_view, name="login"),
    path('logout', views.logout_view, name="logout"),
    path('create-user', views.create_user, name="create-user"),
    path('create-job', views.create_job, name="create-job"),
    path('report', views.report_by_date, name="report"),
    path('profile', views.profile, name="profile"),
    path('edit-job/<int:jobId>', views.edit_job, name="edit-job"),
    path('delete-job', views.delete_job, name="delete-job"),
    path('update-profile', views.update_profile, name="update-profile"),
    path('search', views.search, name="search"),
    path('send-mail', views.send_еmail, name="send-mail"),
    re_path(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),
]