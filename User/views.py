from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login,logout



from User.models import User
from User.forms import RegisterForm


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            user.username = form.cleaned_data['email']
            user.save()
            return redirect('login')
    else:
        form = RegisterForm()

    return render(request, 'register.html', context={'form': form})


def login_view(request):
    print(request.method)
    print(request.user.is_authenticated)
    # print("$"*80)
    if not request.user.is_authenticated:
        if request.method == "POST":
            user_name = request.POST.get('username')
            user_pass = request.POST.get('password')
            # form = AuthenticationForm(request=request,data=request.POST)
            # if form.is_valid():
                # form = form.cleaned_data['username']
                # form = form.cleaned_data['password']
            user = authenticate(username=user_name, password=user_pass)
            print(user)
            print("*"*80)
            if user is not None:
                login(request, user)
                return redirect('dashboard')
        else:
            return render(request, 'login.html', {})
    else:
        return render(request, 'login.html', {})
    
def logout_request(request):
    logout(request)
    return redirect("login")


def dashboard(request):
    return render(request, 'dashboard.html', {})
