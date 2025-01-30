from django.shortcuts import render

# Create your views here.
# authentication/views.py
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .forms import CustomUserCreationForm

# Inscription
def signup(request):
    if request.method == "POST":
        #form = UserCreationForm(request.POST)
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("home")  # Rediriger vers la page d'accueil ou une autre page
    else:
        form = UserCreationForm()
    return render(request, "registration/signup.html", {"form": form})

# Connexion
def signin(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("home")  # Rediriger vers la page d'accueil
    else:
        form = AuthenticationForm()
    return render(request, "registration/signin.html", {"form": form})

# Déconnexion
def signout(request):
    logout(request)
    return redirect("signin")  # Rediriger vers la page de connexion


# authentication/views.py
def home(request):
    return render(request, 'home.html')  # Utilise ton propre template ici
