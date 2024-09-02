from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from main.function import superuser_required, center_create, get_models_list, center_edit
from main.models import Center


@login_required
@superuser_required
def view_centers(request):
    if request.method == 'POST':
        return center_create(request)
    content = get_models_list(request)
    return render(request, 'center/view_center.html', context=content)


@login_required
@superuser_required
def center_edit_view(request, center_id):
    center = Center.objects.get(pk=center_id)
    if request.method == 'POST':
        return center_edit(request, center)
    content = get_models_list(request)
    content['center_edit'] = center
    return render(request, 'center/center_update.html', context=content)


@login_required
@superuser_required
def delete_center(request, center_id):
    center = Center.objects.get(id=center_id)
    center.delete()
    return redirect('main:centers')

