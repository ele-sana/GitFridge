from django.shortcuts import render
from django.http import HttpResponse
from FridgeApp.models import Aliments, Recettes
# Create your views here.

def Welcome(request):
    welcome = "Bienvenue dans le  frigo d'Eléonor et Alain. <br> Vous allez pouvoir concocter votre repas en fonction des aliments de votre  frigo.<br> Vous pourrez égalemnet vous inspirer par nos recettes sur le site   "
    return HttpResponse(welcome)

def FooDListing(request):
    aliments = Aliments.objects.order_by("-name")[:3]
    formatedAliments = ["<ul><li style='text-align:center' type='check-box'>{}</li></ul>".format(aliment.name) for aliment in aliments]
    context = {'aliments': aliments}
    return HttpResponse(aliments,context)

def RecettesListing(request):
    recettes = Recettes.objects.order_by("-name")[:3]
    formatedRecettes = ["<ul><li style='text-align:center' type='check-box'>{}</li></ul>".format(recette.name) for recette in recettes]
    context = {'recettes': recettes,
    'thumbnail':recettes.picture}
    return HttpResponse(recettes,context)
    


