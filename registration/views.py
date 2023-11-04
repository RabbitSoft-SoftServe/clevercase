from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login, logout
from django.contrib.auth.decorators import login_required

from wallet.forms import CategoryCreateForm
from wallet.models import Category

@login_required(login_url='login')
def home_page(request):
    print("home_page")
    if request.method == 'POST':
        form = CategoryCreateForm(request.POST, request=request)
        if form.is_valid():
            category = form.save(commit=False)  # Создаем объект, но не сохраняем его в базу данных
            category.user = request.user  # Устанавливаем поле 'user'
            category.save()  # Теперь сохраняем в базу данных

            return redirect('home')
    else:
        form = CategoryCreateForm()

    categories = Category.objects.filter(user=request.user)
    context = {
        'categories': categories,
        'form': form,
    }
    return render(request, 'homepage.html', context)
def signup_page(request):
    if request.method == 'POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')
        if pass1 != pass2:
            return render(request,'signuperror.html')
        else:
            my_user=User.objects.create_user(uname,email,pass1)
            my_user.save()
            return redirect('login')
    return render(request,'signup.html')

def LoginPage(request):
    if request.method== 'POST':
        username = request.POST.get('username')
        pass1= request.POST.get('pass')
        user=authenticate(request, username=username,password=pass1)
        if user is not None:
            login(request, user) 
            return redirect('home')
        else:
            return render(request, 'loginerror.html', {'user': 0})
    return render (request, 'login.html')

def LogoutPage(request):
    logout(request)
    return redirect('login')

def landing_page(request):
    return render(request, 'landing.html')