from Blog import views
from django.urls import path
from . import views

urlpatterns=[
    path('utilisateurs/',views.utilisateur_view,name='utilisateurs')
]