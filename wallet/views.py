from django.shortcuts import render
from .forms import CategoryForm


def my_view(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = CategoryForm()
    return render(request, 'homepage.html', {'form': form})