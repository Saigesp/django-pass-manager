# -*- coding: utf-8 -*-
import os
from django.contrib.auth import login, update_session_auth_hash, authenticate, views as auth_views
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.decorators import login_required, permission_required, user_passes_test
from django.shortcuts import render, redirect

"""
LOGIN
"""
def custom_login(request):

    if request.user.is_authenticated():
        return redirect('home')

    return auth_views.login(request)


"""
CHANGE PASSWORD
"""
@login_required(login_url='/login/')
def change_password(request):
    data = {}

    if request.method == 'POST':
        data['form'] = PasswordChangeForm(request.user, request.POST)
        if data['form'].is_valid():
            user = data['form'].save()
            update_session_auth_hash(request, user)  # Important!
            print 'Contraseña cambiada'
            return redirect('home')
    else:
        print 'Contraseña no cambiada'
        data['form'] = PasswordChangeForm(request.user)

    return render(request, 'registration/password_change.html', data)



"""
HOME
"""
@login_required(login_url='/login/')
def home(request):
    data = {}

    return render(request, 'home.html', data)