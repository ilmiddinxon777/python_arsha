from django.shortcuts import render
from myfiles.models import *

# Create your views here.

def index(malumot):
    if 'message' in malumot.POST:
        ismi = malumot.POST.get("name")
        gmail = malumot.POST.get("email")
        mavzu = malumot.POST.get("subject")
        text = malumot.POST.get("message")
        Contact(name=ismi,email=gmail,subject=mavzu,text=text).save()


    elif 'gmail' in malumot.POST:
        qoshish = malumot.POST.get('gmail')
        Subscribe(email=qoshish).save()



    ports =Portfolio.objects.all()
    servi = services.objects.all()
    team = Team.objects.all()
    return render(malumot, "index.html", {"ports":ports, "servi":servi, "team":team})

def portfoler(malumot, id):
    port = Portfolio.objects.get(id=id)
    return render(malumot, "portfolio-details.html", {"port":port})

def inner_page(malumot):
    return render(malumot, 'inner-page.html')



