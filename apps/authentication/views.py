from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.contrib.auth.models import User

def login_view(request):
    if request.method == 'POST':
        print(request.POST)
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        print(user)
        form = AuthenticationForm(data=request.POST)
        # print(form)
        if user:
            login(request, user)
            # return redirect('/api/v1/admin')
            return JsonResponse({'success': True})
    else:
        form = AuthenticationForm()
    return render(request, 'authentication/login.html', {'form': form})

def dashboard_view(request):
    return render(request, 'layouts/dashboard.html')

def register_view(request):
    if request.method == 'POST':
        print(request.POST)
        name = request.POST.get('name')
        lastname = request.POST.get('lastname')
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = User.objects.create_user(username=email, email=email, password=password,first_name=name, last_name=lastname)
        print(user)

        form = AuthenticationForm(data=request.POST)
        if user:
            # login(request, user)
            # return redirect('/api/v1/admin')
            return JsonResponse({'success': True})
            # return render(request, 'authentication/login.html', {'form': form})
    else:
        form = AuthenticationForm()
    return render(request, 'authentication/registers.html', {'form': form})

@login_required
def dashboard_view(request):
    return render(request, 'layouts/dashboard.html')

@login_required
def logout_view(request):
    logout(request)
    return redirect('login')
