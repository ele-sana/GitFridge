from django.shortcuts import render
from django.http import HttpResponse
from FridgeApp.models import Aliments, Recettes, NameForm
from django.template import loader
# Create your views here.
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage



def FooDListing(request):
    aliments = Aliments.objects.all().order_by("name")
    # formatedAliments = ["<ul><li style='text-align:center' type='check-box'>{}</li></ul>".format(aliment.name) for aliment in aliments]
    # template = loader.get_template("TemplateFridge/index.html")
    context = {'aliments': aliments}
    return render(request,'TemplateFridge/index.html',context)

def RecettesListing(request): 
    recettes = Recettes.objects.all().order_by("-name")    # template = loader.get_template("TemplateFridge/index.html")
    # formatedRecettes = ["<ul><li style='text-align:center' type='check-box'>{}</li></ul>".format(recette.name) for recette in recettes]
    context = {'recettes': recettes}
    return render(request,'TemplateFridge/index.html',context)
    
def HowToCook(request):
    howToCook = Recettes.objects.all().order_by("-name")
    context = {'howToCook': howToCook }
    return render(request,'TemplateFridge/index.html',context)

def Listing(request):
    recettesList = Recettes.objects.all()
    paginator = Paginator(recettesList, 5)
    page= request.GET.get('page')
    try:
        recettes = paginator.page(page)
    except PageNotAnInteger:
        recettes = paginator.page(1)
    except EmptyPage:
        recettes = paginator.page(paginator.num_pages)    
    context = {
        'recettes':recettes,
        'paginate' : True
    }
    return render(request,'FridgeApp/listing.html',context)



def Search(request):
    queries = request.GET.getlist('query')
    receipts = Recettes.objects.all()
    recettesQueJePeuxFaire =[]
    name =""
    for receipt in receipts :
        alimentNbr = 0
        for rAliment in receipt.aliments.all():
            for query in queries :
                if query == rAliment.name:
                    alimentNbr+=1
        name += receipt.name + " : " + str(alimentNbr) + "/" +  str(len(receipt.aliments.all()))       
        if alimentNbr == len(receipt.aliments.all()):
            recettesQueJePeuxFaire.append(receipt)
            

    query = ""
    for q in queries:
        query += q + ", "


    # name = "Résultats pour la recherche %s" %query
    context = { 
     'recettes' : recettesQueJePeuxFaire,
    'name': name 
    }
    return render (request,'TemplateFridge/search.html', context)



def getChoice(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            return render('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()
    context = {'form' : form}
    return render(request, 'FridgeApp/search.html', context)