from django.contrib import admin
from .models import Biografiya, Index, Add, Site
from django.contrib.auth.models import User, Group

# Register your models here.
admin.site.unregister(User)
admin.site.unregister(Group)


@admin.register(Biografiya)
class HojixonBiography(admin.ModelAdmin):
    list_display = ('name', 'description', 'bio')


@admin.register(Add)
class HojixonAdd(admin.ModelAdmin):
    list_display = ('name', 'description', 'bio')


@admin.register(Index)
class HojixonIndex(admin.ModelAdmin):
    list_display = ('name', 'year', 'info')


@admin.register(Site)
class HojixonSite(admin.ModelAdmin):
    list_display = ('title',)