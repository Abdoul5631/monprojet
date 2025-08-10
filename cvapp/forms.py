from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser
from .models import CV
from taggit.forms import TagWidget
from django.contrib.auth import get_user_model

# Formulaire pour les CV
class CVForm(forms.ModelForm):
    class Meta:
        model = CV
        fields = [
            'full_name',
            'email',
            'phone',
            'summary',
            'skills',
            'experience',
            'education',
            'profession',
            'bio',
            'address',
            'category',
            'tags',
        ]
        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Entrez votre nom complet'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Entrez votre adresse e-mail'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Entrez votre numéro de téléphone'}),
            'summary': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Résumé professionnel'}),
            'skills': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Listez vos compétences'}),
            'experience': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Décrivez votre expérience professionnelle'}),
            'education': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Décrivez votre formation académique'}),
            'profession': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Votre profession actuelle'}),
            'bio': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Décrivez brièvement votre biographie'}),
            'linkedin': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'Lien vers votre profil LinkedIn'}),
            'github': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'Lien vers votre profil GitHub'}),
            'address': forms.Textarea(attrs={'class': 'form-control', 'rows': 2, 'placeholder': 'Votre adresse complète'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'tags': TagWidget(attrs={'class': 'form-control', 'placeholder': 'Ajoutez des tags'}),
        }

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not email.endswith('@example.com'):
            raise forms.ValidationError("L'adresse e-mail doit se terminer par @example.com")
        return email

User = get_user_model()  # Récupère dynamiquement le modèle utilisateur
class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'password1', 'password2']

