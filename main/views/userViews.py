from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from main.function import login_function, superuser_required, content_need, delete_user


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
    content['users'] = User.objects.all()
    return render(request, 'user/users.html', context=content)


@login_required
@superuser_required
def view_user(request, user_id):
    if request.method == 'POST':
        return delete_user(request, user_id)    # xatolik ++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    content = get_user_function(request, user_id)
    return render(request, 'user/user_view.html', context=content)


@login_required
@superuser_required
def delete_user_view(request, pk):
    return delete_user(request, pk)



@login_required
@superuser_required
def create_user_view(request):
    content = content_need(request)
    content['centers'] = Center.objects.all()
    content['users'] = User.objects.all()
    if request.method == 'POST':
        return create_user(request)
    return render(request, 'user/add_user.html', context=content)

