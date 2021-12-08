from django.shortcuts import render
from django.http import HttpResponse
from FridgeApp.models import Aliments, Recettes
from django.template import loader
# Create your views here.



def FooDListing(request):
    aliments = Aliments.objects.all().order_by("-name")[:3]
    # formatedAliments = ["<ul><li style='text-align:center' type='check-box'>{}</li></ul>".format(aliment.name) for aliment in aliments]
    # template = loader.get_template("TemplateFridge/index.html")
    context = {'aliments': aliments}
    return render(request,'TemplateFridge/index.html',context)

def RecettesListing(request):
    recettes = Recettes.objects.all().order_by("-name")[:3]
    # template = loader.get_template("TemplateFridge/index.html")
    # formatedRecettes = ["<ul><li style='text-align:center' type='check-box'>{}</li></ul>".format(recette.name) for recette in recettes]
    context = {'recettes': recettes}
    return render(request,'TemplateFridge/index.html',context)
    


