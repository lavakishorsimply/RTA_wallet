"""RTA_Wallet URL Configuration

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
from django.contrib import admin
from django.urls import path
from registration import views as r1
from app1 import views as a1
urlpatterns = [
    path('admin/', admin.site.urls),
    path('view',r1.add_show,name="addandshow"),
    path('delete/<int:id>/',r1.delete_data,name="deletedata"),
    path('/<int:id>/',r1.update_data,name="updatedata"),

    path('',a1.Sign_Up,name='signup_page'),
    path('login/',a1.user_login,name='login_page'),
    path('main/',r1.add_show,name='main'),
    path('logout/',a1.logout_page,name='logout_page'),




]
