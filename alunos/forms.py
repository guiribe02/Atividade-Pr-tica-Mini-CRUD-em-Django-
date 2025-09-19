from django import forms
from .models import Aluno

class AlunoForm(forms.ModelForm):
    data_nascimento = forms.DateField(
        input_formats=['%d/%m/%Y'],
        widget=forms.DateInput(
            format='%d/%m/%Y',
            attrs={'class': 'form-control', 'placeholder': 'dd/mm/aaaa'}
        )
    )

    class Meta:
        model = Aluno
        fields = ['nome', 'sobrenome', 'data_nascimento', 'curso']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite o nome'}),
            'sobrenome': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite o sobrenome'}),
            'curso': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite o curso'}),
        }
