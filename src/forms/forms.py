from django import forms
from .models import dataFormModels


class formModels(forms.ModelForm):
    class Meta:
        model = dataFormModels
        fields = ['name', 'email', 'message', 'isRead']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'mt-1 block w-full px-4 py-3 border border-gray-300 rounded-lg shadow-sm focus:ring-green-500 focus:border-green-500 transition duration-150',
                'placeholder': 'Seu nome completo'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'mt-1 block w-full px-4 py-3 border border-gray-300 rounded-lg shadow-sm focus:ring-green-500 focus:border-green-500 transition duration-150',
                'placeholder': 'seu@email.com'
            }),
            'message': forms.Textarea(attrs={
                'class': 'mt-1 block w-full px-4 py-3 border border-gray-300 rounded-lg shadow-sm focus:ring-green-500 focus:border-green-500 transition duration-150',
                'rows': 5,
                'placeholder': 'Digite sua mensagem aqui...'
            }),
        }
        labels = {
            'name': 'Nome Completo',
            'email': 'Email',
            'message': 'Mensagem'
        }