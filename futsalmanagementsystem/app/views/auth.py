from django.shortcuts import render, redirect
from app.models.models import Ground, Team


def login(request):
    return render(request, "login.html")

def homepage(request):
    return render(request , "home.html")

def index(request):
    grounds = Ground.objects.all()
    teams = Team.objects.all()
    return render(request, "index.html", {'grounds': grounds, 'teams': teams})

def entry(request):
    request.session['email'] = request.POST['email']
    request.session['password'] = request.POST['password']
    request.session.set_expiry(300)
    return redirect("/user")


def logout(request):
    del request.session['email']
    del request.session['password']
    return redirect("/")
