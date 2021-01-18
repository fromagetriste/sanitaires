from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.utils import timezone

from .parsing import formater_message_frais
from .models import FichierFrais
from .forms import FichierFraisForm
from .autodetele import supprimer_fichiers


def sanitaires(request):
    #supprimer_fichiers() # pour supprimer tous les fichiers stockés (loop and delete)
    if request.method == 'POST':
        form = FichierFraisForm(request.POST, request.FILES)
        if form.is_valid():
            #fichier_a_traiter = request.FILES['message_frais'] #pas besoin d'ouvrir le fichier car il est ouvert
            #for x in fichier_a_traiter:   
            #    print(x)
            form.save()
            return redirect('success')
    else:
        form = FichierFraisForm()
    return render(request, 'sanitaires/sanitaires.html', {
        'form' : form
        })


def success(request):
    form_recu = FichierFrais.objects.latest('pk')
    chemin_message_frais = form_recu.message_frais.path
    formater_message_frais(chemin_message_frais)
    url_du_fichier_xlsx = str(form_recu.message_frais.url[:-4] + '.xlsx')
    return render(request, 'sanitaires/success.html', {
        'form_recu' : form_recu,
        'url_du_fichier_xlsx' : url_du_fichier_xlsx
        })

