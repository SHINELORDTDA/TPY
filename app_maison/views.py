
from django.shortcuts import redirect, render # type: ignore
from django.http import HttpResponse # type: ignore
from .models import Maison
from app_quartier.models import Quartier  # ✅ Quartier vient de l'autre app
from django.contrib import messages # type: ignore


def home(request):
    return render(request, 'app_maison/home.html')

 # filepath: c:\Users\yvann\Desktop\yvanna_django\app_maison\views.py
from django.shortcuts import render # type: ignore

def enregistrer_quartier(request):
    # Logique pour enregistrer un quartier
    return render(request, 'app_maison/enregistrer_quartier.html')

def home(request):
    quartiers = Quartier.objects.all()
    maisons = Maison.objects.all()
    return render(request, 'app_maison/home.html', {
        'quartiers': quartiers,
        'maisons': maisons,
    })

# Autres vues (optionnelles, à compléter selon ton besoin)
def liste_maisons(request):
    maisons = Maison.objects.all()
    return render(request, 'app_maison/liste_maisons.html', {'maisons': maisons})

def enregistrer_maison(request):
    ...
    messages.error(request, "Superficie des maisons supérieure à celle du quartier !")

    
def formulaire_maison(request):
    return render(request, 'formulaire_maison.html')






def formulaire_quartier(request):
    return render(request, 'formulaire_quartier.html')




def enregistrer_maison(request):
    if request.method == "POST":
        proprietaire = request.POST.get('proprietaire')
        superficie = float(request.POST.get('superficie'))
        adresse = request.POST.get('adresse')
        prix = float(request.POST.get('prix'))
        chambres = int(request.POST.get('chambres'))
        quartier_id = request.POST.get('quartier')  # à ajouter dans le form

        try:
            quartier = Quartier.objects.get(id=quartier_id)
        except Quartier.DoesNotExist:
            messages.error(request, "Quartier introuvable.")
            return redirect('formulaire_maison')

        superficie_totale = sum(m.superficie for m in quartier.maisons.all())

        if superficie_totale + superficie > quartier.superficie:
            messages.error(request, "⚠️ Superficie des maisons supérieure à celle du quartier !")
            messages.warning(request, "Redéfinir les superficies des maisons.")
            return redirect('formulaire_maison')  # ou afficher à nouveau le formulaire

        Maison.objects.create(
            proprietaire=proprietaire,
            superficie=superficie,
            adresse=adresse,
            prix=prix,
            chambres=chambres,
            quartier=quartier
        )
        messages.success(request, "Maison enregistrée avec succès.")
        return redirect('home')
