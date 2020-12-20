from django import forms
from .models import FichierFrais

class FichierFraisForm(forms.ModelForm):
    class Meta:
        model = FichierFrais
        fields = ('titre', 'message_frais',)

