from django.shortcuts import render, redirect, RequestContext
from django.contrib.auth.decorators import login_required
from .forms import ProfileForm, PortfolioForm
from .models import Developer, Portfolio
from shared_files.DevBoxUser import get_object_or_none
# from azure.blob.storage import BlobService
# from Register_Developer.blob_data import *
# Create your views here.

# this directs you to the developers profile page i.e. /profile/me


@login_required(login_url='/dev/')
def profile(request):
    developer = Developer.objects.filter(id=request.user.id)
    portfolio = Portfolio.objects.filter(owner_id=request.user.id)
    context = RequestContext(request, {'developer': developer,
                             'portfolio': portfolio})
    print(developer, portfolio)
    return render(request, 'profile.html', context=context)


# this line edits the current user by pre loading their details
# from github i.e names and email
@login_required(login_url='/dev/')
def edit_profile(request):
    developer_profile = get_object_or_none(Developer, pk=request.user.pk)
    profile_form = ProfileForm(instance=developer_profile)
    return render(request, 'register.html',
                  context={'profile_form': profile_form})


@login_required(login_url='/dev/')
def new_portfolio(request):
    portfolio_form = PortfolioForm
    return render(request, 'register_portfolio.html',
                  context={'portfolio_form': portfolio_form})

# this is where we create the user


@login_required(login_url='/dev/')
def create_profile(request):
    developer_profile = get_object_or_none(Developer, pk=request.user.pk)
    profile_form = ProfileForm(request.POST or None,
                               instance=developer_profile)
    if request.method == 'POST':
        if profile_form.is_valid():
            profile_form.save()
            return redirect('/dev/profile/me/')
    return render(request, 'register.html',
                  context={'profile_form': profile_form})


@login_required(login_url='/dev/')
def create_portfolio(request):
    # dev = Developer.objects.get(pk=request.user._get_pk_val)
    portfolio_form = PortfolioForm(request.POST, request.FILES)
    if request.method == 'POST':
        if portfolio_form.is_valid():
            portfolio = portfolio_form.save(commit=False)
            portfolio.owner_id = request.user.id
            portfolio.save()
            # upload_portfolio_image()
            portfolio_form.save_m2m()
            portfolio = Portfolio.objects.get(owner_id=request.user.id)
            developer = Developer.objects.get(id=request.user.id)
            print(developer.first_name)
            return redirect('/dev/profile/me/',
                            context={portfolio:
                                     'portfolio', developer: 'developer'})
    return render(request, 'register_portfolio.html',
                  context={'portfolio_form': portfolio_form})

# uploading portfolios to azure
# def upload_portfolio_image(path):
#     blob = BlobService(account_name=ACCOUNT_NAME,account_key=ACCOUNT_KEY)
#     blob.put_block_blob_from_path('images',BLOB_NAME,path,x_ms_blob_content_type='{}{}{}'.format('image','/','png')
