from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from .forms import RegpayCreateForm
from .models import Regpay

@login_required(login_url='login')
def regpay_page(request):
    if request.method == 'POST':
        form = RegpayCreateForm(request.POST, request=request)
        if form.is_valid():
            form.save()

            context = {
                'form': RegpayCreateForm(),
            }
            return render(request, 'regularpays.html', context)
    form = RegpayCreateForm()
    regpays = Regpay.objects.filter(user=request.user)
    context = {
        'form': form,
        'regpay': regpays,
    }
    return render(request, 'regularpays.html', context)