from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, HttpResponseRedirect
from .forms import SignUpForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout


# Create your views here.
def Sign_Up(request):
    if request.method == "POST":
        fm = SignUpForm(request.POST)
        if fm.is_valid():
            messages.success(request, 'Account created sucessfully')
            fm.save()
    else:
        fm = SignUpForm()
    return render(request, 'signup.html', {'form': fm})


def user_login(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            fm = AuthenticationForm(request=request, data=request.POST)
            if fm.is_valid():
                uname = fm.cleaned_data['username']
                upass = fm.cleaned_data['password']
                user = authenticate(username=uname, password=upass)
                if user is not None:
                    login(request, user)
                    messages.success(request, 'Logged in sucessfully !!')
                    return HttpResponseRedirect('/main/')
        else:
            fm = AuthenticationForm()
        return render(request,'userlogin.html',{'form': fm})
    else:
        return HttpResponseRedirect('/login')


def profile_page(request):
    if request.user.is_authenticated:
        return render(request, 'profile.html', {'name': request.user})
    else:
        return HttpResponseRedirect('/login/')


def logout_page(request):
    logout(request)
    return HttpResponseRedirect('/signup_page')

