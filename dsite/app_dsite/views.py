from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Dsite
from .forms import AdvertisementForm
from django.urls import reverse, reverse_lazy
from django.contrib.auth.decorators import login_required


def index(requests):
    advertisements = Dsite.objects.all()
    context = {'advertisements': advertisements}
    return render(requests, 'app_advertisement/index.html', context)

def top_sellers(request):
    return render(request, 'app_advertisement/top-sellers.html')
@login_required(login_url=reverse_lazy('profile'))
def advertisement_post(request):
    if request.method == 'POST':
        form = AdvertisementForm(request.POST, request.FILES)
        if form.is_valid():
            advertisement = form.save(commit=False)
            advertisement.user = request.user
            advertisement.save()
            url = reverse('main-page')
            return redirect(url)
    else:
        form = AdvertisementForm()
    context = {'form': form}
    return render(request, 'app_advertisement/advertisement-post.html', context)

def register(request):
    return render(request, 'app_auth/register.html')

def login(request):
    return render(request, 'app_auth/login.html')

def profile(request):
    return render(request, 'app_auth/profile.html')


