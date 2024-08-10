from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from online_shop.forms import LoginFrom, RegisterForm


def login_page(request):
    if request.method == 'POST':
        form = LoginFrom(request.POST)
        if form.is_valid():
           username = form.cleaned_data.get('username')
           password = form.cleaned_data.get('password')
           user =  authenticate(request,username=username,password=password)
           if user:
              login(request,user)
              return redirect('index')
           else:
                messages.error(request,'Invalid username or password')

    else:
         form=LoginFrom()
    return  render(request,'online_shop/auth/login.html',{'form': form })
def register_page(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user=form.save(commit=True)
            login(request,user)
            return redirect('index')

        else:
            print(form.errors)
    else:
        form = RegisterForm()
    return render(request,'online_shop/auth/register.html',{'form': form})

def logout_page(request):
    if request.method == 'POST':
       logout(request)
       return redirect('index')