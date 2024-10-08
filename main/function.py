from datetime import datetime
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect
from .models import Center, Manager, ControlCard, Group, Reporter, DocumentType, AuthorResolution, TypeSolution, \
    CheckFile, Letter, ControlFile
from django.contrib.auth.models import User


def login_function(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect('main:welcome')
    else:
        return redirect('main:login')


def content_need(request):
    user = User.objects.get(username=request.user.username)
    center = Center.objects.get(user=user)
    if center.user.is_superuser:
        managers = Manager.objects.all()
    else:
        managers = Manager.objects.filter(center=center)

    total = managers.count()
    in_control = 0
    done = 0
    expired = 0
    has_deadline = 0
    for man in managers:
        if not man.control and man.control_file:
            in_control += 1
        if man.control:
            done += 1
        if man.time_off and not man.control and not man.control_file:
            expired += 1
        if not man.time_off:
            has_deadline += 1

    content = {
        'center': center,
        'managers': managers,
        'total': total,
        'in_control': in_control,
        'done': done,
        'expired': expired,
        'has_deadline': has_deadline,
        'users': User.objects.all(),
    }
    return content


def manager_today(request):
    content = content_need(request)
    manager = content['managers']
    managers = []
    for man in manager:
        if man.time_today:
            managers.append(man)
    content['managers'] = managers
    return content


def manager_control(request):
    content = content_need(request)
    manager = content['managers']
    managers = []
    for man in manager:
        if man.control:
            managers.append(man)
    content['managers'] = managers
    return content


def manager_out(request):
    content = content_need(request)
    manager = content['managers']
    managers = []
    for man in manager:
        if man.time_off:
            managers.append(man)
    content['managers'] = managers
    return content


def get_models_list(request):
    content = content_need(request)
    content = {
        'managers': content['managers'],
        'center': content['center'],
        'total': content['total'],
        'in_control': content['in_control'],
        'done': content['done'],
        'expired': content['expired'],
        'has_deadline': content['has_deadline'],
        'centers': Center.objects.all(),  # Markazlar.
        'control_cards': ControlCard.objects.all(),  # Тип контрольной карточки Nazorat kartasining turi
        'groups': Group.objects.all(),  # Группа Guruh
        'reporters': Reporter.objects.all(),  # Корреспондент Muhbir
        'document_types': DocumentType.objects.all(),  # Тип документа Hujjat turi
        'author_resolutions': AuthorResolution.objects.all(),  # # Автор резолюции Qaror muallifi
        'type_solutions': TypeSolution.objects.all(),  # Вид решения Yechim turi
        'users': User.objects.all()
    }
    return content


def create_check_file(request):
    file = request.FILES['check_file']
    check_file = CheckFile.objects.create(file=file)
    check_file.save()
    return check_file


def update_manager(request, manager):
    if manager.control_file:
        control = True if request.POST.get('control') == 'True' else False
        manager.control = control
    else:
        file = request.FILES['control_file']
        control_file = ControlFile.objects.create(file=file)
        control_file.save()
        manager.control_file = control_file
    summary = request.POST['summary']
    type_solution = TypeSolution.objects.get(pk=int(request.POST['type_solution']))
    letter = Letter.objects.get(id=manager.letter.id)
    letter.summary = summary
    letter.control = True
    letter.type_solution = type_solution
    letter.save()
    manager.letter = letter
    manager.save()
    return redirect('main:welcome')


def get_centers_post(request):
    center_id = request.POST.getlist('centers')
    centers = []
    for center in center_id:
        centers.append(Center.objects.get(pk=int(center)))
    return centers


def get_selects(request):
    control_card = ControlCard.objects.get(pk=int(request.POST['control_card']))
    group = Group.objects.get(pk=int(request.POST.get('group')))
    reporter = Reporter.objects.get(pk=int(request.POST.get('reporter')))
    document_type = DocumentType.objects.get(pk=(request.POST.get('document_type')))
    auth_resolution = AuthorResolution.objects.get(pk=int(request.POST.get('auth_resolution')))
    type_solution = TypeSolution.objects.get(pk=int(request.POST.get('type_solution')))
    selects = {
        'control_card': control_card,
        'group': group,
        'reporter': reporter,
        'document_type': document_type,
        'auth_resolution': auth_resolution,
        'type_solution': type_solution
    }
    return selects


def create_letter(request, selects):
    letter = Letter.objects.create(
        control_card=selects['control_card'],
        group=selects['group'],
        reporter=selects['reporter'],
        document_type=selects['document_type'],

        registration_date=request.POST['registration_date'],
        registration_number=request.POST['registration_number'],

        document_number=request.POST['document_number'],
        document_date=request.POST['document_date'],

        resolution=request.POST['resolution'],
        auth_resolution=selects['auth_resolution'],
        type_solution=selects['type_solution']
    )
    if letter:
        letter.save()
        return letter
    else:
        return redirect('main:manager-add')


def manager_create(request, content):
    centers = content['centers']
    for center in centers:
        manager = Manager.objects.create(
            letter=content['letter'],
            check_file=content['file'],
            lifetime=request.POST.get('lifetime'),
            center=center
        )
        manager.save()

    return redirect('main:welcome')


def superuser_required(view_func):
    """
    Decorator for views that checks whether the user is a superuser,
    and returns HttpResponseForbidden if not.
    """

    def _wrapped_view(request, *args, **kwargs):
        if not request.user.is_superuser:
            return redirect('main:welcome')
        return view_func(request, *args, **kwargs)

    return _wrapped_view


def create_user(request):
    first_name = request.POST['full_name']
    username = request.POST['username']
    password = request.POST['password']
    conform_password = request.POST['conform_password']
    if password == conform_password:
        user = User.objects.create(
            username=username,
            password=password,
            first_name=first_name,
        )
        if user:
            user.save()
            return redirect('main:users')
        else:
            return redirect('main:add-user')
    else:
        return redirect('main:add-user')


def get_user_function(request, user_id):
    content = content_need(request)
    user = User.objects.get(pk=user_id)
    if request.method == 'POST':
        first_name = request.POST['full_name']
        username = request.POST['username']
        user.first_name = first_name
        user.username = username
        user.save()
        return redirect('main:users')
    content['edit_user'] = user
    return content


def delete_user(request, user_id):
    user = User.objects.get(pk=user_id)
    user.delete()
    return redirect('main:users')


def get_center_edit(request, center_id):
    content = content_need(request)
    center = Center.objects.get(id=center_id)
    content['center_up'] = center
    content['centers'] = Center.objects.all()
    content['users'] = User.objects.all()
    return content


def center_edit(request, center):
    user = User.objects.get(id=int(request.POST['user_id']))
    center.name = request.POST['name']
    center.short = request.POST['short']
    center.user = user
    center.save()
    return redirect('main:centers')


def center_create(request):
    name = request.POST['center_name']
    short = request.POST['center_short']
    try:
        user = User.objects.get(pk=int(request.POST['user_id']))
        center = Center(name=name, short=short, user=user)
    except ValueError:
        center = Center(name=name, short=short)
    center.save()
    return redirect('main:centers')
