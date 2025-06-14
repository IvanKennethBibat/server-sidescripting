from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def begin(request):
    pet = request.GET.get("pet") or "dog"
    return HttpResponse("Hello World, TakeOn - Adopt A Pet " + "<br><h1>The pet requested was " + pet)

def specific_pet(request):
    pet_name = request.GET.get("pet_name") or "Fluffy"
    return render(request, "pet.html", {"pet_name":pet_name})

