from django.shortcuts import render
from .models import Account

# Create your views here.
def dashboard(request):
    accounts = Account.objects.all()
    context = {
        "accounts": accounts,
        "auth": request.user.is_authenticated,
    }
    return render(request, "Accounts/dashboard.html", context)