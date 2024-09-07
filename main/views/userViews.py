from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from main.function import login_function, superuser_required, content_need, delete_user, create_user, get_user_function


def login_view(request):
    if request.method == 'POST':
        return login_function(request)
    return render(request, 'user/login.html')


def logout_view(request):
    logout(request)
    return redirect('main:login')


@login_required
@superuser_required
def view_users(request):
    content = content_need(request)
    return render(request, 'user/users.html', context=content)


@login_required
@superuser_required
def edit_user_view(request, user_id):
    if request.method == 'POST':
        return get_user_function(request, user_id)
    content = get_user_function(request, user_id)
    return render(request, 'user/edit_user.html', context=content)


@login_required
@superuser_required
def delete_user_view(request, user_id):
    user = User.objects.get(pk=user_id)
    user.delete()
    return redirect('main:users')


@login_required
@superuser_required
def create_user_view(request):
    content = content_need(request)
    if request.method == 'POST':
        create_user(request)
    return render(request, 'user/users.html', context=content)

