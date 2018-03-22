from django.shortcuts import render,redirect
from django.contrib.auth import (
    login,
    logout,
    authenticate
)
from django.contrib.auth.models import User
from .models import CustomUser
from .forms import UserLoginForm,UserRegistrationForm
# Create your views here.
def home_view(request):

    return render(request,'base.html',{})


def login_view(request):
    print(request.user.is_authenticated)

    title = "login"

    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        login(request, user)
        return redirect('/')

    context = {
        'form': form,
        'title': title

    }

    return render(request, 'form.html', context)


def logout_view(request):
    logout(request)
    return render(request,'form.html',{})


def register_view(request):
    title="register"
    form=UserRegistrationForm(request.POST or None)
    if form.is_valid():
        user=User()
        username=form.cleaned_data.get('username')
        password=form.cleaned_data.get('password')
        user.username=username
        user.set_password(password)
        user.save()
        new_user = authenticate(username=user.username, password=password)
        custom_user=CustomUser()
        custom_user.user=user
        custom_user.user_type='driver'
        custom_user.save()
        login(request,new_user)


        return redirect('/')

    context={
        'form':form,
        'title':title

    }

    return render(request, 'form.html',context)

