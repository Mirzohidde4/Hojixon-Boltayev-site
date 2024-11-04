from django.shortcuts import render, redirect, get_object_or_404
from .models import Biografiya, Index, Add, Site, Comments

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
    izoh = Comments.objects.all()
    
    if request.method == 'POST':
        comment = request.POST.get('comment')
        user = request.user
        if comment and len(comment.strip()) != 0:
            Comments.objects.create(author=user, comment=comment)
        return redirect('store')  
    
    return render(request, 'store.html', {'store': store, 'site': site, 'izoh': izoh})
