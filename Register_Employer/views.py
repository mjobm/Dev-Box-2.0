from django.shortcuts import (render, RequestContext,
                              redirect, get_object_or_404)
from django.contrib.auth.decorators import login_required
from Register_Employer.models import Employer, JobPost
from Register_Employer.forms import EmployerForm, JobForm
from Register_Developer.models import Developer
from shared_files.DevBoxUser import get_object_or_none
# Create your views here.


@login_required(login_url='/emp/accounts/login/')
def emp_home(request):
    if not get_object_or_none(Developer, id=request.user.id):
        context = {'user': request.user, 'employer': ''}
        save_employer(request)
        if not get_object_or_none(Employer, id=request.user.id).first_name:
            employer_form = EmployerForm(instance=get_object_or_none(Employer,
                                         id=request.user.id))
            return render(request, 'register_emp.html',
                          context={'user': request.user,
                                   'employer_form': employer_form})
        employer = get_object_or_none(Employer, id=request.user.id)
        job = JobPost.objects.filter(owner_id=request.user.id)
        skills = []
        for item in job:
            skills = [skill for skill in item.skills_required.split(',')]
        context = {'user': request.user, 'employer': employer.user,
                   'emp': employer, 'jobs': job, 'skills': skills}
        return render(request, 'emp_home.html', context=context)
    return redirect('/dev/logout', '/emp/accounts/login/')


@login_required(login_url='/emp/accounts/login/')
def register_employer(request):
    emp_details = Employer.objects.get(pk=request.user.pk)
    employer_form = EmployerForm(request.POST or None, instance=emp_details)
    if request.method == 'POST':
        if employer_form.is_valid():
            employer_form.save()
            return redirect('/emp/home/')
    return render(request, 'register_emp.html',
                  context={'employer_form': employer_form})


# this method checks whether an employer exists in the model,
# if None exists then the Employers id, username & email are saved.
def save_employer(request):
    if not get_object_or_none(Employer, pk=request.user.pk):
        emp = Employer()
        emp.pk = request.user.pk
        emp.user = request.user
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
            job_post = job_form.save(commit=False)
            job_post.owner_id = request.user.id
            job_post.save()
            job_form.save_m2m()
            # employer = get_object_or_none(Employer, id=request.user.id)
            # job = JobPost.objects.filter(owner_id=request.user.id)
            # context = {'user': request.user, 'employer': employer.user,
            #            'emp': employer, 'jobs': job}
            # print(job.title)
            return redirect('/emp/home/')
    return render(request, 'post_job.html', context={'job_form': job_form})
