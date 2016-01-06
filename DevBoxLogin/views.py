from django.shortcuts import render_to_response, redirect, render, RequestContext, get_object_or_404
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
from Register_Developer.models import Developer
# Create your views here.
from Register_Employer.models import Employer

def get_started(request):

    return render(request,'get_started.html')
    
def login(request):
    return render(request,'login.html')

@login_required(login_url='/dev/')
def home(request):
    dev_id = None
    emp = None

    try:
        dev_id = Developer.objects.get(pk=request.user.pk)
        emp = get_object_or_404(Employer,id=request.user.id)
    except:
       pass

    print(emp)
    if not emp:
        context = RequestContext(request,{'request':request,'user':request.user})
        if not dev_id:
            dev = Developer()
            dev.pk = request.user.pk
            dev.first_name = request.user.first_name
            dev.last_name = request.user.last_name
            dev.email_address = request.user.email
            dev.is_developer = True
            dev.save()
        return render_to_response('home.html', context_instance=context)
    return redirect('/emp/accounts/logout/', '/dev/')



def logout(request):
    auth_logout(request)
    return redirect('/')
