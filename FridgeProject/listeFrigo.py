# frigo


from FridgeApp.models import Aliments
farine = Aliments.objects.get(name="Farine")
muscade = Aliments.objects.get(name="Muscade")
bacon = Aliments.objects.get(name="Bacon")
paprika = Aliments.objects.get(name="Paprika")
basilic = Aliments.objects.get(name="Basilic")
curry = Aliments.objects.get(name="Curry")
laitConcentre =Aliments.objects.get(name="Lait concentré")
huileOlives  = Aliments.objects.get(name="Huile d'Olives")
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
beurre = Aliments.objects.get(name="Beurre")
lait = Aliments.objects.get(name="Lait")
gruyereRape = Aliments.objects.get(name="Gruyère râpé")
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
ail= Aliments.objects.get(name="Ail")
oignon = Aliments.objects.get(name="Oignons")
echalote = Aliments.objects.get(name="Echalote")
orange = Aliments.objects.get(name="Orange")
vermouth=Aliments.objects.get(name="Verliytg
tomate = Aliments.objects.ger(name="Tomate"
sel= Aliments.objects.get(name="Sel")
poivre=Aliments.objects.get(name="Poivre")
lardons=Aliments.objects.get(name="Lardons")



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


