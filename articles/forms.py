from django import forms
from django.db.models.base import Model
from django.forms import ModelForm, fields
from .models import Article

class ArticleForm(ModelForm):
    class Meta:
        model=Article
        fields = "__all__"
        widgets = {
            'titre': forms.TextInput(
                attrs={
                    'placeholder': 'Nom du pays',
                    'class': 'form-control',
                }
            ),
            'contenu':forms.Textarea(
                attrs={
                    'placeholder':'Informations',
                    'class': 'form-control',
                }
            ),
            'slug':forms.TextInput(
                attrs={
                     'placeholder':'Capital',
                    'class': 'form-control',
                }
            )
            
            }