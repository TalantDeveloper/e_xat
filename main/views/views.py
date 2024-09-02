from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from main.function import content_need


@login_required
def welcome(request):
    content = content_need(request)
    return render(request, 'main/welcome.html', context=content)

