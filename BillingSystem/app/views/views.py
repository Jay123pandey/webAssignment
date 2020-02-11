from django.shortcuts import render, redirect
from app.models.admin import Admin
from app.authentication import Authenticate


def index(request):
    return render(request,"index.html")

@Authenticate.user_valid
def layout(request):
    return render(request,"layout.html")

def entry(request):
	request.session['email']=request.POST['email']
	request.session['password']=request.POST['password']
	return redirect("/layout")
