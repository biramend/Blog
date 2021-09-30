from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def utilisateur_view(request):
    return render(request,'utilisateur/liste_utilisateur.html')