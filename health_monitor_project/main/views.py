from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .models import BloodPressureReading


# Create your views here.

def home(request):
    return render(request, 'home.html')


def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username").strip()
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)
        if user is None:
            return render(request, "login.html", {
                "error": "Invalid username/password"
            })

        login(request, user)
        return redirect("dashboard")

    return render(request, "login.html")

@login_required
def dashboard(request):
    return render(request, "dashboard.html")

def signup_view(request):
    if request.method == "POST":
        first_name = request.POST.get("first_name", "").strip()
        last_name =  request.POST.get("last_name", "").strip()
        email = request.POST.get("email", "").strip()
        password1 = request.POST.get("password1", "")
        password2 = request.POST.get("password2", "")

        if password1 != password2:
            return render(request, "signup.html", {
            "error": "Password do not match."
            })
        if User.objects.filter(username=email).exists():
            return render(request, "signup.html", {
                "error": "Account already exists. Please try again!"
                })

        user = User.objects.create_user(

            username=email,
            email=email,
            password=password1,
            first_name=first_name,
            last_name=last_name,
            )
        login(request, user)
        return redirect("dashboard")

    return render(request, "signup.html")

@login_required
def add_bp(request):
    if request.method == "POST":
        systolic = int(request.POST.get("systolic"))
        diastolic = int(request.POST.get("diastolic"))
        heart_rate_raw = request.POST.get("heart_rate")

        heart_rate = int(heart_rate_raw) if heart_rate_raw else None

        BloodPressureReading.objects.create(
            user=request.user,
            systolic=systolic,
            diastolic=diastolic,
            heart_rate=heart_rate
        )
        return redirect("bp_history")

    return render(request, "add_bp.html")

def bp_history(request):
    readings = BloodPressureReading.objects.filter(user=request.user).order_by("-created_at")
    return render(request, "bp_history.html", {"readings":readings})