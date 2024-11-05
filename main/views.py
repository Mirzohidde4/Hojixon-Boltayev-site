from django.shortcuts import render, redirect, get_object_or_404
from .models import Biografiya, Index, Add, Site, Comments
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate

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
        user = request.user
        if User.objects.filter(username=user).exists():
            comment = request.POST.get('comment')
            if comment and len(comment.strip()) != 0:
                Comments.objects.create(author=user, comment=comment)
            return redirect('store')  
        return redirect('sign')
    return render(request, 'store.html', {'store': store, 'site': site, 'izoh': izoh})


def SignPage(request):
    if request.method == 'POST':
        first_name = request.POST.get('firstname')
        last_name = request.POST.get('lastname')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        if password1 == password2:
            if User.objects.filter(username=username).exists():
                name = 'username exists!'
                return render(request, 'sign.html', {'name': name})
            if User.objects.filter(email=email).exists():
                pochta = 'email address exists!'
                return render(request, 'sign.html', {'pochta': pochta})
            else:
                user = User.objects.create_user(username=username, email=email, password=password1, first_name=first_name, last_name=last_name)
                user.save()
                login(request, user)
                return redirect('index')
        else:
            hato = 'passwords didn\'t match!'
            return render(request, 'sign.html', {'hato': hato})
    return render(request, 'sign.html')


def LoginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            hato = 'username or password error!'
            return render(request, 'login.html', {'hato': hato})
    return render(request, 'login.html')


def LogoutPage(request):
    logout(request)
    return redirect('index')