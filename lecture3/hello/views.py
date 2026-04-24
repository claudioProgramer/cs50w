from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "hello/index.html")

def lepe(request):
    return HttpResponse("Lepe es un pueblo de Huelva, Andalucía, España.")

def david(request):
    return HttpResponse("David es un nombre común en muchos países.")

def greet(request, name):
    return render(request, "hello/greet.html", {
        "name": name.capitalize()  # Capitaliza la primera letra del nombre para una mejor presentación
    })