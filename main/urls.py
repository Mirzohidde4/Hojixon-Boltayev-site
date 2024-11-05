from django.urls import path
from .views import IndexView, AboutView, AddView, StoreView, LoginPage, LogoutPage, SignPage 


urlpatterns = [
    path('', IndexView, name='index'),
    path('about/', AboutView, name='about'),
    path('add/', AddView, name='products'),
    path('store', StoreView, name='store'),
    path('login', LoginPage, name='login'),
    path('sign', SignPage, name='sign'),
    path('logout', LogoutPage, name='logout')
]