# -*- coding: utf-8 -*-
import os
from django.contrib.auth import login, update_session_auth_hash, authenticate, views as auth_views
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.sites.shortcuts import get_current_site
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode

from forms import SignUpForm
from tokens import account_activation_token


"""
LOGIN
"""
def custom_login(request):

    if request.user.is_authenticated():
        return redirect('home')

    messages.success(request, 'Olrait')
    return auth_views.login(request)


"""
SIGN UP
"""
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.username = user.email
            user.save()
            current_site = get_current_site(request)
            subject = 'Activate Your MySite Account'
            message = render_to_string('registration/signup_activation_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            user.email_user(subject, message)
            return redirect('signup_activation_sent')
    else:
        form = SignUpForm()

    return render(request, 'registration/signup.html', {'form': form})



"""
SEND ACTIVATION LINK
"""
def signup_activation_sent(request):

    return render(request, 'registration/signup_activation_sent.html', {})


"""
ACTIVATE ACCOUNT
"""
def signup_activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        return redirect('home')
    else:
        return render(request, 'signup_activation_invalid.html')


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