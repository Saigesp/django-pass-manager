# -*- coding: utf-8 -*-
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views as auth_views

import views

urlpatterns = [

    # LOGIN
    url(r'^$', views.custom_login, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': '/'}, name='logout'),
    url(r'^passwordchange/$', views.change_password, name='change_password'),

    # ADMIN
    url(r'^opensesame/', admin.site.urls, name='opensesame'),

    # HOME
    url(r'^home/', views.home, name='home'),

]