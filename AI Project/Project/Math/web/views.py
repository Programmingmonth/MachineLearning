from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def addition(request):
    return render(request, 'addition.html')  # Addition template

def subtraction(request):
    return render(request, 'subtraction.html')  # Subtraction template

def multiplication(request):
    return render(request, 'multiplication.html')  # Multiplication template

def division(request):
    return render(request, 'division.html')  # Division template