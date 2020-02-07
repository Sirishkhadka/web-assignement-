from app.models.models import User
from django.shortcuts import redirect
from django.db.models import Q
from django.contrib import messages

class Authenticate:

    def valid_user(function):
        def wrap(request):
            try:
                User.objects.get(Q(email=request.session['email']) & Q(password=request.session['password']))
                return function(request)
            except:
                messages.warning(request, 'Please login first...')
                return redirect("/")

        return wrap

    def valid_user_include_id(function):
        def wrap(request,id):
            try:
                User.objects.get(Q(email=request.session['email']) & Q(password=request.session['password']))
                return function(request,id)
            except:
                messages.warning(request, 'Please login first...')
                return redirect("/")

        return wrap
