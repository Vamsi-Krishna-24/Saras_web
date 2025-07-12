from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib.auth.models import User


def Home(request):
    return render(request, 'HomeTemp/home.html')

def Home(request):
    return render(request, 'HomeTemp/home_login.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('Home_login')
        else:
            return render(request, 'HomeTemp/loginP.html', {
                'error': "Invalid username or password"
            })

    return render(request, 'HomeTemp/loginP.html')



def register_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        # Check if passwords match
        if password != confirm_password:
            return render(request, 'HomeTemp/register.html', {
                'error': "Passwords do not match"
            })

        # Check if username already exists
        if User.objects.filter(username=username).exists():
            return render(request, 'HomeTemp/register.html', {
                'error': "Username already taken"
            })

        # Create the user
        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()

        return redirect('login')

    return render(request, 'HomeTemp/register.html')
