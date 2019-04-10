from django.shortcuts import render,redirect
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from sites.forms import LoginForm, SignupForm


# Create your views here.

# def sites(request):
#     return render(request, "sites.html")

def signup(request):

    if request.user.username:
        return redirect(home)

    # pass
    # form = UserCreationForm()
    form = SignupForm()
    message = ""
    if request.method == 'POST':
        # form = UserCreationForm(request.POST)
        form = SignupForm(request.POST)
        if form.is_valid():
            formData = form.cleaned_data
            user = User()
            user.username = formData['username']
            user.email = formData['email']
            user.set_password(formData['password1'])

            # Inserts data to DB as this is ORM function given by Django.
            user.save()
            message = "User signup done successfully!"

    return render(request, 'auth/signup.html', {'form': form, "message": message})

def signin(request):
    if request.user.username:
        return redirect(home)
    # pass
    form = LoginForm()
    message = ""

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            # pass
            formData = form.cleaned_data
            user = authenticate(
                username=formData['username'],
                password=formData['password']
            )
            if user is None:
                message = "Invalid login details!"
            else:
                login(request, user)
                request.session["city"] = 'Bengaluru'
                request.session['address'] = 'BTM'
                return redirect(home)

    return render(request, 'auth/signin.html', {'form': form, "message": message})

def home(request):
    # pass
    return render(request,'auth/home.html')

def sessionLogout(request):
    # pass
    logout(request)
    return redirect(signin)