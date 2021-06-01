"""csi URL Configuration

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
from . import views

urlpatterns = [
    path('', views.login_page, name="login_page"),
    path('login_dashboard', views.login_dashboard, name="login_dashboard"),
    path('dashboard', views.dashboard, name="dashboard"),
    path('logout_admin', views.logout_admin, name="logout_admin"),
    path('user_registration', views.user_registration, name="user_registration"),
    path('check_user_registration', views.check_user_registration, name="check_user_registration"),
    path('assign_task', views.assign_task,name="assign_task"),
    path('impdata',views.impdata,name='impdata'),
    path('review_task',views.review_task,name='review_task'),
    path('udata',views.udata,name='udata'),
    path('see_user',views.see_user,name='see_user'),
    path('deleteuser', views.deleteuser, name="deleteuser"),
    path('change_username', views.change_username, name="change_username"),
    path('check_status', views.check_status, name="check_status"),
    path('show_id', views.show_id, name="show_id"),
    path('change_password', views.change_password, name="change_password"),
    path('update_password', views.update_password, name="update_password"),
    path('login_dashboard2', views.login_dashboard2, name="login_dashboard2"),
    path('check_mail',views.check_mail,name="check_mail"),
    path('check_mail1',views.check_mail1,name="check_mail1"),
    path('forgot_password',views.forgot_password,name="forgot_password"),
    path('About_us',views.About_us,name="About_us"),
    path('get_review',views.get_review,name="get_review"),
    path('del_data',views.del_data,name="del_data"),
    path('report',views.report,name="report"),
    path('feedback',views.feedback,name="feedback"),
]
