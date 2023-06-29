from django.shortcuts import render
from django.http import JsonResponse
from .utils.messageErrors import methodNothAllowed
from .handler.usersHandlers import UserRegistrationView ,LoginView

# Create your views here.

UserRegistration = UserRegistrationView
Login = LoginView

def paymentsEnpoint(request):
    if request.method == 'POST':
        pass
    else:
        return JsonResponse(
            methodNothAllowed.message,
            status=methodNothAllowed.status,
        )