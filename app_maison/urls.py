from django.urls import path # type: ignore

from app_maison import views


urlpatterns = [
    path('creer-maison/', views.formulaire_maison, name='formulaire_maison'),

    path('enregistrer-maison/', views.enregistrer_maison, name='enregistrer_maison'),
    path('creer-quartier/', views.formulaire_quartier, name='formulaire_quartier'),
    path('enregistrer-quartier/', views.enregistrer_quartier, name='enregistrer_quartier'),
] 


from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Assure-toi d'avoir une vue `home` dans views.py
        path('maison/', views.formulaire_maison, name='formulaire_maison'),
    path('quartier/', views.formulaire_quartier, name='formulaire_quartier'),
    path('maisons/', views.liste_maisons, name='liste_maisons'),

]