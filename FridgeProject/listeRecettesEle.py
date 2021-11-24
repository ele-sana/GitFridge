
pateCarbonara = Recettes(name="Pâtes carbonara")
pateCarbonara.save()
chiconGratin = Recettes(name ="Chicon aux gratin")
chiconGratin.save()
gratinDePateAuJambon = Recettes(name ="Gratin de pâtes au jambon")
gratinDePateAuJambon.save()
omeletteCampagnarde = Recettes(name ="Omelette campagnarde")
omeletteCampagnarde.save()
soupeDeHaricotVert = Recettes(name ="Soupe de haricots verts")
soupeDeHaricotVert.save()
tartiflette = Recettes(name ="Tartiflette")
tartiflette.save()
gratindeCourgette = Recettes(name ="Gratin de Courgettes")
gratindeCourgette.save()
bouletsALaLiegeoise= Recettes(name ="Boulets à la Liégeoise")
bouletsALaLiegeoise.save()
cabillaudEnPapillote = Recettes(name ="Cabillaud en papillotes")
cabillaudEnPapillote.save()
carbonadeFlamande = Recettes(name ="Carbonades à la Flamande")
carbonadeFlamande.save()
pouletAigreDoux = Recettes(name ="Poulet aigre-doux")
pouletAigreDoux.save()
tomatesFarcies = Recettes(name ="Tomates farcies")
tomatesFarcies.save()
hachisParmentier = Recettes(name ="Hachis Parmentier")
hachisParmentier.save()



# les photos

chiconGratin= Recettes.objects.get(name ="Chicon aux gratin")
chiconGratin.picture ="https://www.delhaize.lu/fr/file/17185.recipes-single/ab1b17658717113d6691351550c56847/358aef34bc1b421c88e18babebe182c0.jpg"
chiconGratin.save()
gratinDePateAuJambon = Recettes.objects.get(name ="Gratin de pâtes au jambon")
gratinDePateAuJambon.picture="https://assets.afcdn.com/recipe/20161123/34832_w1024h1024c1cx2644cy1872.jpg"
gratinDePateAuJambon.save()
omeletteCampagnarde = Recettes.objects.get(name ="Omelette campagnarde")
omeletteCampagnarde.picture="http://p9.storage.canalblog.com/93/96/163138/8595921.jpg"
omeletteCampagnarde.save()
soupeDeHaricotVert = Recettes.objects.get(name ="Soupe de haricots verts")
soupeDeHaricotVert.picture="https://www.recette360.com/wp-content/uploads/2019/04/Soupe-de-haricots-verts-et-pommes-de-terre-au-thermomix-696x468.jpg"
soupeDeHaricotVert.save()
tartiflette = Recettes.objects.get(name ="Tartiflette")
tartiflette.picture="https://assets.afcdn.com/recipe/20160401/38946_w1024h768c1cx2690cy1793.jpg"
tartiflette.save()
gratindeCourgette = Recettes.objects.get(name ="Gratin de Courgettes")
gratindeCourgette.picture="https://assets.afcdn.com/recipe/20190529/93185_w1024h1024c1cx2736cy1824.jpg"
gratindeCourgette.save()
bouletsALaLiegeoise= Recettes.objects.get(name ="Boulets à la Liégeoise")
bouletsALaLiegeoise.picture="https://gourmandiz.dhnet.be/app/uploads/2018/03/bouletsliegeois.jpg"
bouletsALaLiegeoise.save()
cabillaudEnPapillote = Recettes.objects.get(name ="Cabillaud en papillotes")
cabillaudEnPapillote.picture="https://img.cuisineaz.com/660x660/2017/06/11/i128176-.jpeg"
cabillaudEnPapillote.save()
carbonadeFlamande = Recettes.objects.get(name ="Carbonades à la Flamande")
carbonadeFlamande.picture="https://cac.img.pmdstatic.net/fit/http.3A.2F.2Fprd2-bone-image.2Es3-website-eu-west-1.2Eamazonaws.2Ecom.2Fcac.2F2018.2F09.2F25.2Fbda9f46a-20a2-4bd0-a854-bbd4cca95294.2Ejpeg/750x562/quality/80/crop-from/center/cr/wqkgRnJhbmNpcyBLT01QQUxJVENIL1BSSVNNQVBJWCAvIEN1aXNpbmUgQWN0dWVsbGU%3D/carbonade-flamande.jpeg"
carbonadeFlamande.save()
pouletAigreDoux = Recettes.objects.get(name ="Ooulet aigre-doux")
pouletAigreDoux.picture="https://res.cloudinary.com/hv9ssmzrz/image/fetch/c_fill,f_auto,h_600,q_auto,w_800/https://s3-eu-west-1.amazonaws.com/images-ca-1-0-1-eu/recipe_photos/original/178622/pinterest.png"
pouletAigreDoux.save()
tomatesFarcies = Recettes.objects.get(name ="Tomates farcies")
tomatesFarcies.picture="https://www.papillesetpupilles.fr/wp-content/uploads/2014/08/Tomates-Farcies-HD.jpg"
tomatesFarcies.save()
hachisParmentier = Recettes.objects.get(name ="Hachis Parmentier")
hachisParmentier.picture="https://www.papillesetpupilles.fr/wp-content/uploads/2014/11/Hachis-Parmentier-%C2%A9Liyana-Vynogradova-Shutterstock.jpg"
hachisParmentier.save()

# les recettes
pateCarbonara = Recettes(howToCook="https://www.marmiton.org/recettes/recette_pates-a-la-carbonara_80453.aspx")
pateCarbonara.save()
chiconGratin= Recettes.objects.get(name ="Chicon aux gratin")
chiconGratin.howToCook="https://www.marmiton.org/recettes/recette_endives-chicons-au-gratin-belgique_27819.aspx"
chiconGratin.save()
gratinDePateAuJambon = Recettes.objects.get(name ="Gratin de pâtes au jambon")
gratinDePateAuJambon.howToCook="https://www.marmiton.org/recettes/recette_gratin-de-pates-au-jambon_334460.aspx"
gratinDePateAuJambon.save()
omeletteCampagnarde = Recettes.objects.get(name ="Omelette forestière")
omeletteCampagnarde.howToCook="https://www.marmiton.org/recettes/recette_omelette-campagnarde_82950.aspx"
omeletteCampagnarde.save()
soupeDeHaricotVert = Recettes.objects.get(name ="Soupe de haricots verts")
soupeDeHaricotVert.howToCook="https://www.marmiton.org/recettes/recette_veloute-d-haricots-verts_41016.aspx"
soupeDeHaricotVert.save()
tartiflette = Recettes.objects.get(name ="Tartiflette")
tartiflette.howToCook="https://www.marmiton.org/recettes/recette_tartiflette-facile_15733.aspx"
tartiflette.save()
gratindeCourgette = Recettes.objects.get(name ="Gratin de Courgettes")
gratindeCourgette.howToCook="https://www.marmiton.org/recettes/recette_gratin-de-courgettes-rapide_17071.aspx"
gratindeCourgette.save()
bouletsALaLiegeoise= Recettes.objects.get(name ="Boulette à la Liégeoise")
bouletsALaLiegeoise.howToCook="https://www.marmiton.org/recettes/recette_boulets-a-la-liegeoise_32638.aspx"
bouletsALaLiegeoise.save()
cabillaudEnPapillote = Recettes.objects.get(name ="Cabillaud en papillotes")
cabillaudEnPapillote.howToCook="https://www.marmiton.org/recettes/recette_filet-de-cabillaud-en-papillote_19058.aspx"
cabillaudEnPapillote.save()
carbonadeFlamande = Recettes.objects.get(name ="Carbonades à la Flamande")
carbonadeFlamande.howToCook="https://www.marmiton.org/recettes/recette_carbonades-flamandes-traditionnelles_29711.aspx"
carbonadeFlamande.save()
pouletAigreDoux = Recettes.objects.get(name ="Ooulet aigre-doux")
pouletAigreDoux.howToCook="https://www.marmiton.org/recettes/recette_poulet-aigre-doux_23788.aspx"
pouletAigreDoux.save()
tomatesFarcies = Recettes.objects.get(name ="Tomates farcies")
tomatesFarcies.howToCook="https://www.marmiton.org/recettes/recette_tomates-farcies-facile_63622.aspx"
tomatesFarcies.save()
hachisParmentier = Recettes.objects.get(name ="Hachis Parmentier")
hachisParmentier.howToCook="https://www.marmiton.org/recettes/recette_hachis-parmentier_17639.aspx"
hachisParmentier.save()

k# liens recettes et aliments
pateCarbonara= Recettes.objects.get(name= "Pâtes carbonara")
pateCarbonara.aliments.add(pates,oeuf,lardons,parmesanrapa)
pateCarbonara.save()


