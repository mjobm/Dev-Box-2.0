from django.shortcuts import (render, RequestContext,
                              redirect, get_object_or_404)
from django.contrib.auth.decorators import login_required
from Register_Employer.models import Employer
from Register_Employer.forms import EmployerForm, JobForm
from Register_Developer.models import Developer
# Create your views here.


@login_required(login_url='/emp/accounts/login/')
def emp_home(request):
    # dev = None
    # try:
    #
    # except:
    #     pass
    dev = get_object_or_404(Developer, id=request.user.id or None)
    if not dev:
        context = {'user': request.user}
        save_employer(request)
        emp = Employer.objects.get(id=request.user.id)
        if not emp.first_name:
            employer_form = EmployerForm(instance=emp)
            return render(request, 'register_emp.html',
                          context={'user': request.user,
                                   'employer_form': employer_form})
        return render(request, 'emp_home.html', context=context)
    return redirect('/dev/logout', '/emp/accounts/login/')


@login_required(login_url='/emp/accounts/login/')
def register_employer(request):
    emp_details = Employer.objects.get(id=request.user.id)
    employer_form = EmployerForm(request.POST or None, instance=emp_details)
    if request.method == 'POST':
        if employer_form.is_valid():
            employer_form.save()
            return redirect('/emp/home/')
    return render(request, 'emp_home.html',
                  context={'employer_form': employer_form})


# this method checks whether an employer exists in the model,
# if None exists then the Employers id, username & email are saved.
@login_required(login_url='/emp/accounts/login/')
def save_employer(request):
    emp_id = None
    try:
        emp_id = Employer.objects.get(pk=request.user.pk)
    except:
        print('User does not exist')
    emp = Employer()
    if not emp_id:
        emp.pk = request.user.pk
        emp.user_name = request.user.username
        emp.email_address = request.user.email
        emp.is_employer = True
        emp.save()


@login_required(login_url='/emp/accounts/login/')
def show_job_form(request):
    job_form = JobForm(request.POST or None)
    return render(request, 'post_job.html', context={'job_form': job_form})


@login_required(login_url='/emp/accounts/login/')
def post_job(request):
    job_form = JobForm(request.POST or None)
    if request.method == 'POST':
        if job_form.is_valid():
            job_form.save()
            redirect('/emp/home/')
    return render(request, 'post_job.html', context={'job_form': job_form})
