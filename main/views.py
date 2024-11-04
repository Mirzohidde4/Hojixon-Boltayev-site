from django.shortcuts import render
from .models import Biografiya, Index, Add, Site

# Create your views here.
def IndexView(request):
    biography = Index.objects.first()
    site = Site.objects.first()
    return render(request, 'index.html', {'biography': biography, 'site': site})


def AboutView(request):
    site = Site.objects.first()
    about = Biografiya.objects.first()
    return render(request, 'about.html', {'about': about, 'site': site})


def AddView(request):
    site = Site.objects.first()
    add = Add.objects.first()
    return render(request, 'products.html', {'add': add, 'site': site})


def StoreView(request):
    site = Site.objects.first()
    store = Biografiya.objects.first()
    return render(request, 'store.html', {'store': store, 'site': site})