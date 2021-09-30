import django
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render
from .forms import ContactForm
from django.urls import reverse
from django.core.mail import  send_mail

def hom_view(request):
    return render(request,'accueil.html')

def contact_view(request):
    form = ContactForm()
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            prenom = form.cleaned_data['prenom']
            nom = form.cleaned_data['nom']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            titre = f'Blog | {prenom} {nom} {email}'
            send_mail(titre,message,'nbirame559@gmail.com',['nbirame559@gmail.com'],fail_silently=False,)
            
        return HttpResponseRedirect(reverse('remerciement'))
    context = {'form':form}
    return render(request,'contact.html',context)

def remerciement_view(request):
    return HttpResponse('<h1 style="text-align:center;"> Merci de nous avoir contacter</h1>')

