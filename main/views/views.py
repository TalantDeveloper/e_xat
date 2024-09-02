from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from main.function import content_need, manager_today, manager_control, manager_out, get_models_list, create_letter, \
    get_centers_post, create_check_file, manager_create, update_manager, get_selects
from main.models import ControlCard, Group, Reporter, DocumentType, AuthorResolution, TypeSolution, Manager, Center


@login_required
def welcome(request):
    content = content_need(request)
    return render(request, 'main/welcome.html', context=content)


@login_required
def today_view(request):
    content = manager_today(request)
    return render(request, 'main/welcome.html', context=content)


@login_required
def finish_view(request):
    content = manager_control(request)
    return render(request, 'main/welcome.html', context=content)


@login_required
def manager_out_view(request):
    content = manager_out(request)
    return render(request, 'main/welcome.html', context=content)


@login_required
def create_manager_view(request):
    content = get_models_list(request)
    if request.method == 'POST':
        selects = get_selects(request)
        letter = create_letter(request, selects)
        centers = get_centers_post(request)
        file = create_check_file(request)
        mana = {
            'letter': letter,
            'centers': centers,
            'file': file
        }
        return manager_create(request, mana)
    return render(request, 'main/home_create.html', context=content)


@login_required
def view_manager(request, manager_id):
    manager = Manager.objects.get(id=manager_id)
    if request.method == 'POST':
        return update_manager(request, manager)
    content = get_models_list(request)
    content['manager'] = manager
    return render(request, 'main/home_update.html', context=content)


def handler404_view(request, exception):
    return render(request, 'handler/404.html', status=404)
