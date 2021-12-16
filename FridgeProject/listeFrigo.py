# frigo


from FridgeApp.models import Aliments
farine = Aliments.objects.get(name="Farine")
muscade = Aliments.objects.get(name="Muscade")
bacon = Aliments.objects.get(name="Bacon")
paprika = Aliments.objects.get(name="Paprika")
basilic = Aliments.objects.get(name="Basilic")
curry = Aliments.objects.get(name="Curry")
laitConcentre =Aliments.objects.get(name="Lait concentré")
cubeBouillon = Aliments.objects.get(name="Cube de bouillon")
persil = Aliments.objects.get(name='Persil')
cassonade = Aliments.objects.get(name="Cassonade")
viandeHachee = Aliments.objects.get(name = "Viande Hachée")
chapelure = Aliments.objects.get(name="Chapelure")
siropDeLiege = Aliments.objects.get(name="Sirop de Liège")
citron = Aliments.objects.get(name="Citron")
fondDeSaucePoisson = Aliments.objects.get(name = "Sauce de fond poisson")
thym = Aliments.objects.get(name="Thym")
bouquetGarni = Aliments.objects.get(name="Bouquet garni")
ketchup = Aliments.objects.get(name="Ketchup")
lardFume = Aliments.objects.get(name="Lard fumé")
painDEpices = Aliments.objects.get(name="Pain d'épices")
viandeDeBoeuf = Aliments.objects.get(name="Viande de boeuf")
biereBrune = Aliments.objects.get(name="Bière brune")
moutarde = Aliments.objects.get(name="Moutarde")
vinaigreDeRiz = Aliments.objects.get(name="Vinaigre de riz")
maizena = Aliments.objects.get(name="Maïzena")
filetDePoulet = Aliments.objects.get(name="Filets de poulet")
herbesDeProvence = Aliments.objects.get(name="Herbes de Provence") 
cremeFraiche = Aliments.objects.get(name="Crème fraiche")
reblechon = Aliments.objects.get(name="Reblechon")
lait = Aliments.objects.get(name="Lait")
parmesanrapa = Aliments.objects.get(name="Parmesan rapé")
jambon = Aliments.objects.get(name="Jambon")
pates = Aliments.objects.get(name="Pâtes")
riz = Aliments.objects.get(name="Riz")
pommeDeTerre = Aliments.objects.get(name="Pomme de terre")
carotte = Aliments.objects.get(name="Carottes")
courgette = Aliments.objects.get(name="Courgettes")
poivron = Aliments.objects.get(name="Poivron")
epinard = Aliments.objects.get(name="Epinard")
champignon = Aliments.objects.get(name="champignon")
navet = Aliments.objects.get(name="navet")
aubergine= Aliments.objects.get(name="Aubergine")
choufleur= Aliments.objects.get(name="Choux fleur")
chouDeBruxelles= Aliments.objects.get(name="Choux de Bruxelles")
endive = Aliments.objects.get(name="Endive")
haricot = Aliments.objects.get(name="Haricot")
oignon = Aliments.objects.get(name="Oignons")
echalote = Aliments.objects.get(name="Echalote")
orange = Aliments.objects.get(name="Orange")
vermouth=Aliments.objects.get(name="Verliytg
tomate = Aliments.objects.ger(name="Tomate"




ratatouille.aliments.add(ail,aubergine,courgette,tomate,sel,poivre,huileOlives,oignon)
ratatouille.save()
chouDeBruxellesAuLardons.aliments.add(chouDeBruxelles,echalote,sel,poivre,lardons,muscade,beurre)
chouDeBruxellesAuLardonssave()
FricasseePoulet.aliments.add(ail,vermouth,bouquetGarni,paprika,sel,poivre,huileOlives,persil,poulet,lardons,poivron,oignon)
FricasseePoulet.save()
pouletOrange.aliments.add(champignon,orange,poivre,sel,herbesDeProvence,poulet,citron,lardons)
pouletOrange.save()
epinarCreme.aliments.add(muscade,ail,sel,poivre,epinard,cremeFraiche,beurre)
epinarCreme.save()
desDeNavetsBeurre.aliments.add(beurre,sel,poivre,navet,oignon)
desDeNavetsBeurre.save()
gratinDeChouFleur.aliments.add(farine,cubeBouillon,sel,poivre,muscade,chouxFleur,beurre,fromageRape,cremeFraiche)
gratinDeChouFleur.save()



ciboulette = Aliments(name="Ciboulette")
ciboulette.save()
ciboulette = Aliments.objects.get(name="Ciboulette")
huileOlives  = Aliments.objects.get(name="Huile d'Olives")
gruyereRape = Aliments.objects.get(name="Gruyère râpé")
courgette = Aliments.objects.get(name="Courgettes")
sel= Aliments.objects.get(name="Sel")
poivre=Aliments.objects.get(name="Poivre")
lardons=Aliments.objects.get(name="Lardons")
beurre = Aliments.objects.get(name="Beurre")
ail= Aliments.objects.get(name="Ail")
oeufs = Aliments.objects.get(name="Oeufs")
pommeDeTerre = Aliments.objects.get(name="Pomme de Terre")



omeletteNature=Recettes(name="Omelette nature")
omeletteNature.save()
omeletteNature=Recettes.objects.get(name="Omelette nature")
omeletteNature.picture="https://assets.afcdn.com/recipe/20100120/22445_w768h583c1cx256cy192.webp"
omeletteNature.howToCook="https://www.marmiton.org/recettes/recette_omelette-nature_21255.aspx"
omeletteNature.save()
omeletteNature.aliments.add(sel,poivre,oeuf,beurre)
omeletteNature.save()


omelettePdtLardons=Recettes(name="Omelette aux pommes de terre et lardons")
omelettePdtLardons.save()
omelettePdtLardons=Recettes.objects.get(name="Omelette aux pommes de terre et lardons")
omelettePdtLardons.picture="https://assets.afcdn.com/recipe/20200220/107931_w1200h800c1cx2880cy1920cxb5760cyb3840.webp"
omelettePdtLardons.howToCook="https://www.marmiton.org/recettes/recette_omelette-aux-pommes-de-terre-et-lardons_19387.aspx"
omelettePdtLardons.save()
omelettePdtLardons.aliments.add(sel,poivre,oeufs,pommeDeTerre,lardons,huileOlive)
omelettePdtLardons.save()

omeletteCourgette=Recettes(name="Omelette aux courgettes râpées")
omeletteCourgette.save()
omeletteCourgette=Recettes.objects.get(name="Omelette aux courgettes râpées")
omeletteCourgette.picture="https://assets.afcdn.com/recipe/20190410/90647_w768h583c1cx3963cy2690cxb6000cyb4000.webp"
omeletteCourgette.howToCook="https://www.marmiton.org/recettes/recette_omelette-aux-courgettes-rapees_60317.aspx"
omeletteCourgette.save()
omeletteCourgette.aliments.add(gruyereRape,sel,oeufs,huileOlive,courgette,ciboulette,ail)
omeletteCourgette.save()

=Aliments(name="")
.save()
=Aliments.objects.get()
.picture=''
.howToCook=""
.save()
.aliments.add()
.save()