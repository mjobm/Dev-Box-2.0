from django.shortcuts import (render_to_response, redirect, render,
                              RequestContext, get_object_or_404)
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
from Register_Developer.models import Developer
# Create your views here.
from Register_Employer.models import Employer
from shared_files.DevBoxUser import get_object_or_none


def get_started(request):
    return render(request, 'get_started.html')


def login(request):
    return render(request, 'login.html')


@login_required(login_url='/dev/')
def home(request):
    # if not employer check whether the user exists
    employer = get_object_or_none(Employer, pk=request.user.pk)
    if not employer:
        context = RequestContext(request, {})
        # if the user does not exists save him as a dev
        if not get_object_or_none(Developer, id=request.user.id):
            save_employer(request)
        developer = get_object_or_none(Developer, id=request.user.id)
        context = RequestContext(request, {'developer': developer.user})
        # return the user to the home page
        return render_to_response('home.html', context_instance=context)
    # else the user is an existing user so he must logout first so that they
    # can continue.
    return redirect('/emp/accounts/logout/', '/dev/home/')


# function that saves the developer
def save_employer(request):
    if not get_object_or_none(Developer, pk=request.user.pk):
        dev = Developer()
        dev.pk = request.user.pk
        dev.user = request.user
        dev.first_name = request.user.first_name
        dev.last_name = request.user.last_name
        dev.email_address = request.user.email
        dev.is_developer = True
        dev.save()


# function to logout
def logout(request):
    auth_logout(request)
    return redirect('/')
