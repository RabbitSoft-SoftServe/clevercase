from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect

from .forms import CategoryCreateForm
from .models import Category
from django.contrib.auth.models import User


@login_required
def category_create_view(request):
    if request.method == 'POST':
        
        form = CategoryCreateForm(request.POST, request=request)
        if form.is_valid():
            form.save()
            return redirect('home') 
    else:
        form = CategoryCreateForm()
    
    context = {
        'form': form,
    }
    return render(request, 'homepage.html', context)