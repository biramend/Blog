from django import forms

class ContactForm(forms.Form):
    prenom = forms.CharField(max_length=100,
        widget=forms.TextInput(
                attrs={
                    'placeholder': 'Votre prenom',
                    'class': 'form-control',
                }
            )
    )
    nom = forms.CharField(max_length=100,
        widget=forms.TextInput(
                attrs={
                    'placeholder': 'Votre nom',
                    'class': 'form-control',
                }
            
    ))
    email = forms.EmailField(
        widget=forms.EmailInput(
                attrs={
                    'placeholder': 'Votre email',
                    'class': 'form-control',
                }
            )
    )
    message = forms.CharField(widget=forms.Textarea(
                attrs={
                    'placeholder': 'Votre message',
                    'class': 'form-control',
                }
            ))

     