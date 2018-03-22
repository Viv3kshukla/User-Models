from django.shortcuts import render,redirect
from django.contrib.auth import (
    authenticate,
    logout,
    login,
)
from .forms import UserLoginForm,UserRegistrationForm
# Create your views here.

def home_view(request):
    return render(request,'home.html',{})


def login_veiw(request):
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
        user=form.save(commit=False)
        password=form.cleaned_data.get('password')
        user.set_password(password)
        user.save()
        login(request,user)
        return redirect('/')

    context={
        'form':form,
        'title':title,
    }

    return render(request, 'form.html',context)
