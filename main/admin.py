from django.contrib import admin
from .models import Biografiya, Index, Add, Site, Comments
from django.contrib.auth.models import User, Group
from unfold.admin import ModelAdmin

# Register your models here.
admin.site.unregister(User)
admin.site.unregister(Group)


@admin.register(Biografiya)
class HojixonBiography(ModelAdmin):
    list_display = ('name', 'description', 'bio')


@admin.register(Add)
class HojixonAdd(ModelAdmin):
    list_display = ('name', 'description', 'bio')


@admin.register(Index)
class HojixonIndex(ModelAdmin):
    list_display = ('name', 'year', 'info')


@admin.register(Site)
class HojixonSite(ModelAdmin):
    list_display = ('title', 'name', 'description')


@admin.register(Comments)
class HojixonSite(ModelAdmin):
    list_display = ('author', 'comment', 'created')
    list_filter = ['created',]