from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from store.models import Supplier, Buyer


@login_required(login_url='login')
def dashboard(request):
    total_supplier = Supplier.objects.count()
    total_buyer = Buyer.objects.count()
    context = {
        'supplier': total_supplier,
        'buyer': total_buyer,
    }
    return render(request, 'dashboard.html', context)
