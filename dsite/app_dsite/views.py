from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Dsite
from .forms import AdvertisementForm, RegisterForm
from django.urls import reverse, reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from django.contrib.auth import get_user_model
from django.db.models import Count

User = get_user_model()

def index(request):
    title = request.GET.get('query')
    if title:
        advertisements = Dsite.objects.filter(title__icontains=title)
    else:
        advertisements = Dsite.objects.all()
    context = {'advertisements': advertisements, 'title': title}
    return render(request, 'app_advertisement/index.html', context)

def top_sellers(request):
    users = User.objects.annotate(adv_count=Count('dsite')).order_by('-adv_count')
    context = {'users': users}
    return render(request, 'app_advertisement/top-sellers.html', context)
@login_required(login_url=reverse_lazy('login'))
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


def advertisement_detail(request, pk):
    advertisement = Dsite.objects.get(id=pk)
    context = {'advertisement': advertisement}
    return render(request, 'app_advertisement/advertisement.html', context)


