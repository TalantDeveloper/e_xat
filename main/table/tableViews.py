from xml.dom.minidom import Document

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from main.function import superuser_required, content_need
from main.models import *


@login_required
@superuser_required
def control_card_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        control_card = ControlCard.objects.create(name=name)
        control_card.save()
        return redirect("table:control_cards")
    control_cards = ControlCard.objects.all()
    context = {'control_cards': control_cards}
    return render(request, 'tables/control_cards.html', context)


@login_required
@superuser_required
def control_card_update(request, pk):
    if request.method == 'POST':
        name = request.POST.get('name')
        control_card = ControlCard.objects.get(pk=pk)
        control_card.name = name
        control_card.save()
        return redirect("table:control_cards")
    control_card = ControlCard.objects.get(pk=pk)
    control_cards = ControlCard.objects.all()
    context = {'control_cards': control_cards, 'control_card': control_card}
    return render(request, 'tables/control_cards.html', context)


@login_required
@superuser_required
def control_card_delete(request, pk):
    control_card = ControlCard.objects.get(pk=pk)
    control_card.delete()
    return redirect("table:control_cards")


@login_required
@superuser_required
def groups_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        group = Group.objects.create(name=name)
        group.save()
        return redirect("table:groups")
    groups = Group.objects.all()
    context = {'groups': groups}
    return render(request, 'tables/groups.html', context)


@login_required
@superuser_required
def groups_update(request, pk):
    if request.method == 'POST':
        name = request.POST.get('name')
        group = Group.objects.get(pk=pk)
        group.name = name
        group.save()
        return redirect("table:groups")
    group = Group.objects.get(pk=pk)
    groups = Group.objects.all()
    context = {'groups': groups, 'group': group}
    return render(request, 'tables/groups.html', context)


@login_required
@superuser_required
def groups_delete(request, pk):
    group = Group.objects.get(pk=pk)
    group.delete()
    return redirect("table:groups")


@login_required
@superuser_required
def reporters_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        reporter = Reporter.objects.create(name=name)
        reporter.save()
        return redirect("table:reporters")
    reporters = Reporter.objects.all()
    context = {'reporters': reporters}
    return render(request, 'tables/reporters.html', context)


@login_required
@superuser_required
def reporters_update(request, pk):
    if request.method == 'POST':
        name = request.POST.get('name')
        reporter = Reporter.objects.get(pk=pk)
        reporter.name = name
        reporter.save()
        return redirect("table:reporters")
    reporter = Reporter.objects.get(pk=pk)
    reporters = Reporter.objects.all()
    context = {'reporters': reporters, 'reporter': reporter}
    return render(request, 'tables/reporters.html', context)


@login_required
@superuser_required
def reporters_delete(request, pk):
    reporter = Reporter.objects.get(pk=pk)
    reporter.delete()
    return redirect("table:reporters")


@login_required
@superuser_required
def document_types_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        document_type = DocumentType.objects.create(name=name)
        document_type.save()
        return redirect("table:document_types")
    document_types = DocumentType.objects.all()
    context = {'document_types': document_types}
    return render(request, 'tables/document_types.html', context)


@login_required
@superuser_required
def document_types_update(request, pk):
    if request.method == 'POST':
        name = request.POST.get('name')
        document_type = DocumentType.objects.get(pk=pk)
        document_type.name = name
        document_type.save()
        return redirect("table:document_types")
    document_type = DocumentType.objects.get(pk=pk)
    document_types = DocumentType.objects.all()
    context = {'document_types': document_types, 'document_type': document_type}
    return render(request, 'tables/document_types.html', context)


@login_required
@superuser_required
def document_types_delete(request, pk):
    document_type = DocumentType.objects.get(pk=pk)
    document_type.delete()
    return redirect("table:document_types")


@login_required
@superuser_required
def author_resolutions_view(request):
    if request.method == "POST":
        name = request.POST.get('name')
        author_resolution = AuthorResolution.objects.create(name=name)
        author_resolution.save()
        return redirect("table:author_resolutions")

    author_resolutions = AuthorResolution.objects.all()
    context = {'author_resolutions': author_resolutions}
    return render(request, 'tables/author_resolutions.html', context)


@login_required
@superuser_required
def author_resolutions_update(request, pk):
    if request.method == 'POST':
        name = request.POST.get('name')
        author_resolution = AuthorResolution.objects.get(pk=pk)
        author_resolution.name = name
        author_resolution.save()
        return redirect("table:author_resolutions")
    author_resolutions = AuthorResolution.objects.all()
    author_resolution = AuthorResolution.objects.get(pk=pk)
    context = {'author_resolutions': author_resolutions, 'author_resolution': author_resolution}
    return render(request, 'tables/author_resolutions.html', context)


@login_required
@superuser_required
def author_resolutions_delete(request, pk):
    author_resolution = AuthorResolution.objects.get(pk=pk)
    author_resolution.delete()
    return redirect("table:author_resolutions")


@login_required
@superuser_required
def type_solutions_view(request):
    if request.method == "POST":
        name = request.POST.get('name')
        type_solution = TypeSolution.objects.create(name=name)
        type_solution.save()
        return redirect("table:type_solutions")
    type_solutions = TypeSolution.objects.all()
    context = content_need(request)
    context['type_solutions'] = type_solutions
    return render(request, 'tables/type_solutions.html', context)


@login_required
@superuser_required
def type_solutions_update(request, pk):
    if request.method == 'POST':
        name = request.POST.get('name')
        type_solution = TypeSolution.objects.get(pk=pk)
        type_solution.name = name
        type_solution.save()
        return redirect("table:type_solutions")
    context = content_need(request)
    type_solution = TypeSolution.objects.get(pk=pk)
    context['type_solutions'] = TypeSolution.objects.all()
    context['type_solution'] = type_solution
    return render(request, 'tables/type_solutions.html', context)


@login_required
@superuser_required
def type_solutions_delete(request, pk):
    type_solution = TypeSolution.objects.get(pk=pk)
    type_solution.delete()
    return redirect("table:type_solutions")
