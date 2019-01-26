from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm , forms
from django.contrib.auth import login,logout


# # Create your views here.
def NGO_signup_view(request):
    if request.method=='POST':
        form = UserSignupForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect('home')

def NGO_login_view(request):


def NGO_logout_view(request):        