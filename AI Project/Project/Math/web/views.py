from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def Math(request):
    return render(request, 'Math.html')  # Math template