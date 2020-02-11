from django.shortcuts import render, redirect
from app.models.admin import Admin
from django.db.models import Q
from django.contrib import messages


class Authenticate:
    def user_valid(function):
        def wrap(request):
            try:
                user = Admin.objects.get(Q(email=request.session['email']) & Q(password=request.session['password']))
                return function(request)

            except:
                return redirect("/")

        return wrap

    def valid_user_include_id(function):
        def wrap(request, id):
            try:
                Admin.objects.get(email=request.session['email'], password=request.session['password'])
                return function(request, id)
            except:

                return redirect('/')

        return wrap

