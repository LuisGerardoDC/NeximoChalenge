from django.shortcuts import render
from django.http import JsonResponse
from .handler.usersHandlers import UserRegistrationView ,LoginView
from .handler.paymentsHandlers import CalculatePayment

# Create your views here.

UserRegistration = UserRegistrationView
Login = LoginView
Calculate = CalculatePayment
