# -*- coding: utf-8 -*-
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views as auth_views

import views

urlpatterns = [

    # ADMIN
    url(r'^opensesame/', admin.site.urls, name='opensesame'),

    # LOGIN
    url(r'^login/$', views.custom_login, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': '/'}, name='logout'),

    # REGISTER
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^signup_activation_sent/$', views.signup_activation_sent, name='signup_activation_sent'),
    url(r'^signup_activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        views.signup_activate, name='signup_activate'),

    # PASSWORD CHANGE
    url(r'^password_change/$', views.change_password, name='change_password'),

    # PASSWORD RESET
    url(r'^password_reset/$', auth_views.password_reset, name='password_reset'),
    url(r'^password_reset/done/$', auth_views.password_reset_done, name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',auth_views.password_reset_confirm, name='password_reset_confirm'),
    url(r'^reset/done/$', auth_views.password_reset_complete, name='password_reset_complete'),


    # HOME
    url(r'^$', views.home, name='home'),

]