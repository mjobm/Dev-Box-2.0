from django.shortcuts import render, RequestContext

def home_page(request):
    context = RequestContext(request,{request.user: 'user' })
    return render(request,'home_page.html',context=context)

def get_started(request):
    return render(request,'get_started.html')
