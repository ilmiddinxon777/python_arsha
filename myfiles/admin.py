from django.contrib import admin

# Register your models here.

from myfiles.models import *

class adminservices(admin.ModelAdmin):
    list_display = ["img", "name", "malumot", "date"]

admin.site.register(services,adminservices)


class admintype(admin.ModelAdmin):
    list_display = ["turi"]

admin.site.register(Type, admintype)

class adminportfolio(admin.ModelAdmin):
    list_display = ["img", "name", "type", "category", "client", "date", "link"]

admin.site.register(Portfolio, adminportfolio)

class adminkasbi(admin.ModelAdmin):
    list_display = ["hodim"]

admin.site.register(Kasbi, adminkasbi)

class adminteam(admin.ModelAdmin):
    list_display = ["name", "kasbi", "malumot", "img", "twit", "face", "inst", "tele", "date"]

admin.site.register(Team, adminteam)


class AdminContact(admin.ModelAdmin):
    list_display = ["name","email", "subject", "text", "date"]

admin.site.register(Contact, AdminContact)


class AdminSubscribe(admin.ModelAdmin):
    list_display = ['email',"date"]

admin.site.register(Subscribe, AdminSubscribe)