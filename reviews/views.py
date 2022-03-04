from django.shortcuts import render

# Create your views here.
def mainMeny(request):
    return render(request,'Hoved.html')
def start(request):
    masiven=[
        {"Name":"Burger","iVerdi":0,"LevId":"BurgerAntal","prisId1":"BurgerPris" , "link":"images/lunch/burger(lunsj).jpg", "butId":"bstBurger", "pris":5, "idBox":"BurgerBox", "info":"En sandwich bestående av en bolle delt i to og en hakket stekt kotelett. I tillegg til kjøtt kan en hamburger ha et bredt utvalg av pålegg, for eksempel ketchup og majones, en skive courgette, salat, syltet agurk, rå eller stekt løk og tomat."},
        {"Name":"Buter","iVerdi":1,"LevId":"ButerAntal" , "prisId1":"ButerPris" ,"link":"images/lunch/buter(lunsj).webp", "butId":"bstButer", "pris":6.50, "idBox":"ButerBox", "info":"En brødskive eller rundstykker fylt eller toppet med et fyll av et spiseklar produkt eller en kombinasjon av begge. En populær type snack på grunn av enkel tilberedning, enkel å spise og bære."},
        {"Name":"Salat","iVerdi":2,"LevId":"SalatAntal" , "prisId1":"SalatPris" ,"link":"images/lunch/salat(lunsj).jpg", "butId":"bstSalat", "pris":5.50, "idBox":"SalatBox","info":"En kald rett med biter av grønnsaker, urter, forskjellige andre planter, sopp, med tillegg av krydder. En salat er enhver kombinasjon av ingredienser som har en dressing eller krydder, eller begge deler."},
        {"Name":"Suppe","iVerdi":3,"LevId":"SuppeAntal" , "prisId1":"SuppePris" ,"link":"images/lunch/suppe(lunsj).jpg", "butId":"bstSuppe", "pris":3, "idBox":"SuppeBox","info":"En rett som inneholder minst 50 % væske. Suppe er en viktig komponent i menneskelig mat, og tjener som en kilde til energi og materiale for å bygge organer og vev i kroppen."},
        {"Name":"Grøt","iVerdi":4,"LevId":"KasjaAntal" , "prisId1":"GrotPris" ,"link":"images/lunch/kasja(lunsj).jpg", "butId":"bstKasja", "pris":2.50, "idBox":"KasjaBox","info":"Flytende, tykk eller smuldrende mat, frokostblandinger kokt i vann eller melk, en rett med kokte frokostblandinger eller mel."},
    ]
    return render(request, 'Lunsjmeny.html', {"AllInfo":masiven})

def butiken(request):
    masiven=[
        {"Name": "Ost kuler","Del":1,"DivInformation":"OstkulerInfo","namm":"one","choseId":"Ostkuleridee","iVerdi":5,"LevId":"OstkulerAntal","prisId1": "OstkulerPris","link": "images/middagsmeny/forrett/Ostkuler.jpg", "butId": "bstOstkuler", "pris": 10, "idBox": "OstkulerBox","info":"Deilige osteboller som vanligvis serveres i høytiden, passer veldig godt for de som ikke har tenner eller elsker snacks."},
        {"Name": "Кeker","Del":2,"DivInformation":"КekerInfo","namm":"one","choseId":"Кekeridee", "iVerdi": 6, "LevId": "КekerAntal", "prisId1": "КekerPris","link":"images/middagsmeny/forrett/krevetki.jpg","butId": "bstКeker", "pris": 5, "idBox": "КekerBox","info":"det er en sjømat som konsumeres over hele verden. Selv om reker og reker er i forskjellige underordner av Decapoda, er de veldig like i utseende og begrepene brukes ofte om hverandre i kommersielt oppdrett og i naturen."},
        {"Name": "Fisk","Del":3,"DivInformation":"FiskInfo","namm":"one","choseId":"Fiskidee", "iVerdi": 7, "LevId": "FiskAntal", "prisId1": "FiskPris","link":"images/middagsmeny/forrett/FiskBrod.jpg","butId": "bstFisk", "pris": 2, "idBox": "FiskBox","info":"Fisk er en god kilde til næringsstoffer som protein, vitamin B12, jod og selen. Fisk, spesielt de halvfete fiskene som rødspette, steinbit og kveite og fete fisker som laks, makrell, sild, ørret, ål, kveite og sardiner er hovedkilde til de marine omega-3 fettsyrene i kostholdet."},
        {"Name": "Plov","Del":4,"DivInformation":"PlovInfo","namm":"two","choseId":"Plovidee","iVerdi":8,"LevId":"PlovAntal","prisId1": "PlovPris","link": "images/middagsmeny/Hovedrett/Plov.jpg", "butId": "bstPlov", "pris": 10, "idBox": "PlovBox","info":"En orientalsk rett basert på kokt ris. Et særtrekk ved pilaf er dens sprøhet, oppnådd ved å observere riskokingsteknologien og tilsette animalsk eller vegetabilsk fett til pilaffen, noe som forhindrer korn i å feste seg sammen."},
        {"Name": "Killing","Del":5,"DivInformation":"KillingInfo","namm":"two","choseId":"Killingidee", "iVerdi": 9, "LevId": "KillingAntal", "prisId1": "KillingPris","link":"images/middagsmeny/Hovedrett/kiling.jpg","butId": "bstKilling", "pris": 15, "idBox": "KillingBox","info":"Fried chicken, også kjent som southern fried chicken, er en rett som består av kyllingbiter som har blitt belagt med krydret mel eller røre og pannestekt, frityrstekt, trykkstekt eller luftstekt."},
        {"Name": "Salat med Fisk","Del":6,"DivInformation":"Fisk_og_SalatInfo","namm":"two","choseId":"Fisk_og_Salatidee", "iVerdi": 10, "LevId": "FiskSalatAntal", "prisId1": "FiskSalatPris","link":"images/middagsmeny/Hovedrett/fiskMedSalat.jpg","butId": "bstFiskSalat", "pris": 1200, "idBox": "FiskSalatBox","info":"Fisk er en god kilde til næringsstoffer som protein, vitamin B12, jod og selen. Fisk, spesielt de halvfete fiskene som rødspette, steinbit og kveite og fete fisker som laks, makrell, sild, ørret, ål, kveite og sardiner er hovedkilde til de marine omega-3 fettsyrene i kostholdet."},
        {"Name": "Pudding","Del":7,"DivInformation":"PuddingInfo","namm":"tree","choseId":"Puddingidee","iVerdi":11,"LevId":"PuddingAntal","prisId1": "PuddingPris","link": "images/middagsmeny/Deserts/Pudding.jpg", "butId": "bstPudding", "pris": 3, "idBox": "PuddingBox","info":"Engelsk wienerbrød. Engelsk pudding inneholder vanligvis finhakket bifftalg, kokte gulrøtter og saueost. De er pakket inn i oljet lin og kokt i saltvann; konsumeres med vin eller saus."},
        {"Name": "Jogurt","Del":8,"DivInformation":"JogurtInfo","namm":"tree","choseId":"Jogurtidee", "iVerdi": 12, "LevId": "JogurtAntal", "prisId1": "JogurtPris","link":"images/middagsmeny/Deserts/Jogurt.jpg","butId": "bstJogurt", "pris": 3, "idBox": "JogurtBox","info":" Fermentert melkeprodukt med høyt tørrstoffinnhold, produsert ved fermentering med en protosymbiotisk blanding av rene kulturer av Streptococcus thermophilus"},
        {"Name": "Kake","Del":9,"DivInformation":"KakeInfo","namm":"tree","choseId":"Kakeidee", "iVerdi": 13, "LevId": "KakeAntal", "prisId1": "KakePris","link":"images/middagsmeny/Deserts/Kake.png","butId": "bstKake", "pris": 17, "idBox": "KakeBox","info":"Et konfektprodukt bestående av flere kaker dynket i krem ​​eller syltetøy. På toppen av kaken er vanligvis dekorert med krem, glasur eller frukt."},
    ]
    return render(request, 'Middagsmeny.html',{"Masiv":masiven})


def tilbakeMening(request):
    masiven1=[
        {"Name": "Rødvin", "choseId": "Rodvin", "iVerdi": 14, "LevId": "RodvinAntal", "prisId1": "RodvinPris",
        "link": "images/drikke/vin/Rødvin.jpg", "butId": "bstRodvin", "pris": 5, "idBox": "RodvinBox"},
        {"Name": "Hvitvin", "choseId": "Hvitvin", "iVerdi": 15, "LevId": "HvitvinAntal", "prisId1": "HvitvinPris",
        "link": "images/drikke/vin/Hvitvin.jpg", "butId": "bstHvitvin", "pris": 8, "idBox": "HvitvinBox"},
        {"Name": "Musserende vin", "choseId": "Musserende_vin", "iVerdi": 16, "LevId": "Musserende_vinAntal", "prisId1": "Musserende_vinPris",
        "link": "images/drikke/vin/Musserende_vin.jpg", "butId": "bstMusserende_vin", "pris": 10, "idBox": "Musserende_vinBox"},
        ]
    masiven2=[
        {"Name": "Lys Øl", "choseId": "Lys_Ol", "iVerdi": 17, "LevId": "Lys_OlAntal", "prisId1": "Lys_OlPris",
        "link": "images/drikke/Ol/HvitOl.jpg", "butId": "bstLys_Ol", "pris": 7, "idBox": "Lys_OlBox",},
        {"Name": "Pale Øl", "choseId": "PaleOl", "iVerdi": 18, "LevId": "PaleOlAntal", "prisId1": "PaleOlPris",
        "link": "images/drikke/Ol/BelgianAle.jpg", "butId": "bstPaleOl", "pris": 5, "idBox": "PaleOlBox"},
        {"Name": "Belgian Øl", "choseId": "BelgianOl", "iVerdi": 19, "LevId": "BelgianOlAntal", "prisId1": "BelgianOlPris",
        "link": "images/drikke/Ol/PaleAle.jpg", "butId": "bstBelgianOl", "pris": 2, "idBox": "BelgianOlBox"},
        ]
    masiven3=[
        {"Name": "Vann", "choseId": "Vann", "iVerdi": 20, "LevId": "VannAntal", "prisId1": "VannPris",
        "link": "images/drikke/Mineral/vann.jpg", "butId": "bstVann", "pris": 1, "idBox": "VannBox"},
        {"Name": "Fanta", "choseId": "Fanta", "iVerdi": 21, "LevId": "FantaAntal", "prisId1": "FantaPris",
        "link": "images/drikke/Mineral/Fanta.jpg", "butId": "bstFanta", "pris": 2, "idBox": "FantaBox"},
        {"Name": "Coca-Cola", "choseId": "CocaCola", "iVerdi": 22, "LevId": "CocaColaAntal", "prisId1": "CocaColaPris",
        "link": "images/drikke/Mineral/CocaCola.jpg", "butId": "bstCocaCola", "pris": 2, "idBox": "CocaColaBox"},
        ]
    antal=[
        {"Id":"div1","Name":"Vin"},
        {"Id":"div2","Name":"Øl"},
        {"Id":"div3","Name":"MineralVann"},
        ]
    return render(request, 'Drikkemeny.html',{"Masiv1":masiven1,"Masiv2":masiven2,"Masiv3":masiven3,"AntalDiver":antal})

def Bordbestilling(request):
    print (request)
    return render(request, 'Bordbestilling.html',)
