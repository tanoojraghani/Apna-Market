from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def display_home(request):
    return render(request, 'Home.html')


def display_market(request):
    return render(request, 'Market.html')


def display_fprofile(request):
    return render(request, 'FarmerProfile.html')


def display_tutorial(request):
    return render(request, 'Tutorial.html')


def display_login(request):
    return render(request, 'Login.html')


def display_register(request):
    return render(request, 'Register.html')


def display_wholesale(request):
    return render(request, 'Wholesale.html')


def display_wprofile(request):
    return render(request, 'WholesaleProfile.html')


def display_employment(request):
    return render(request, 'Employment.html')


def display_eprofile(request):
    return render(request, 'EmploymentProfile.html')


def display_support(request):
    return render(request, 'Support.html')
