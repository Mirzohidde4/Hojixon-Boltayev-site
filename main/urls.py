from django.urls import path
from .views import IndexView, AboutView, AddView, StoreView


urlpatterns = [
    path('', IndexView, name='index'),
    path('about/', AboutView, name='about'),
    path('add/', AddView, name='products'),
    path('store', StoreView, name='store'),
]