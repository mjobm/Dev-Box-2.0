from django.shortcuts import render, RequestContext
from shared_files.DevBoxUser import get_object_or_none
from Register_Developer.models import Developer
from Register_Employer.models import Employer


def home_page(request):
    developer = get_object_or_none(Developer, pk=request.user.pk)
    employer = get_object_or_none(Employer, pk=request.user.pk)
    context = {'user': request.user}
    if developer:
        context = {'user': request.user, 'developer': developer.user}
    else:
        context = {'user': request.user, 'employer': employer}
    return render(request, 'home_page.html', context=context)


def get_started(request):
    developer = get_object_or_none(Developer, pk=request.user.pk)
    employer = get_object_or_none(Employer, pk=request.user.pk)
    context = {'user': request.user}
    if developer:
        context = {'user': request.user, 'developer': developer.user}
    else:
        context = {'user': request.user, 'employer': employer}
    return render(request, 'get_started.html', context=context)
