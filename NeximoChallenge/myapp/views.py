from django.shortcuts import render
from django.http import JsonResponse
from .utils.messageErrors import methodNothAllowed
from .handler.usersHandlers import UserRegistrationView

# Create your views here.

UserRegistration = UserRegistrationView

def paymentsEnpoint(request):
    if request.method == 'POST':
        pass
    else:
        return JsonResponse(
            methodNothAllowed.message,
            status=methodNothAllowed.status,
        )

def loginEndpoint(request):
    if request.method == 'POST':
        pass
    else:
        return JsonResponse(
            methodNothAllowed.message,
            status=methodNothAllowed.status,
        )