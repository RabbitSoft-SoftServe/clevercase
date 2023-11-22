from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login, logout
from django.contrib.auth.decorators import login_required
from wallet.forms import CategoryCreateForm, MyDebtsCreateForm, OthersDebtsCreateForm
from wallet.models import Category, MyDebts, OthersDebts


  
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


def regpay_page(request):
    return render(request, 'regularpays.html')

def debts_menu(request):
    if request.method == 'POST':
        my_debts_form = MyDebtsCreateForm(request.POST, request=request)
        others_debts_form = OthersDebtsCreateForm(request.POST, request=request)
        if my_debts_form.is_valid():
            debt = my_debts_form.save(commit=False)  # Создаем объект, но не сохраняем его в базу данных
            debt.user = request.user  # Устанавливаем поле 'user'
            debt.save()  # Теперь сохраняем в базу данных

            return redirect('debts')
        if others_debts_form.is_valid():
            debt = others_debts_form.save(commit=False)  # Создаем объект, но не сохраняем его в базу данных
            debt.user = request.user  # Устанавливаем поле 'user'
            debt.save()  # Теперь сохраняем в базу данных

            return redirect('debts')
    else:
        my_debts_form = MyDebtsCreateForm()
        others_debts_form = OthersDebtsCreateForm()

    my_debts = MyDebts.objects.filter(user=request.user)
    others_debts = OthersDebts.objects.filter(user=request.user)
    context = {
        'others_debts_form': others_debts_form,
        'my_debts_form': my_debts_form,
        'my_debts': my_debts,
        'others_debts': others_debts,
    }
    return render(request, 'debts.html', context)
