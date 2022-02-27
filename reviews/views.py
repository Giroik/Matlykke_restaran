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
        {"Name": "Ratatouille","Del":1,"DivInformation":"RatatouilleInfo","namm":"one","choseId":"Ratatouilleidee","iVerdi":5,"LevId":"RatatouilleAntal","prisId1": "RatatouillePris","link": "images/middagsmeny/forrett/Ratatui.jpg", "butId": "bstRatatouille", "pris": 10, "idBox": "RatatouilleBox","info":"Ratatouille er en tradisjonell grønnsaksrett av provençalsk mat laget av pepper, aubergine og zucchini, på mange måter lik den ungarske lechoen."},


        {"Name": "Кeker","Del":2,"DivInformation":"КekerInfo","namm":"one","choseId":"Кekeridee", "iVerdi": 6, "LevId": "КekerAntal", "prisId1": "КekerPris","link":"images/middagsmeny/forrett/krevetki.jpg","butId": "bstКeker", "pris": 5, "idBox": "КekerBox","info":"det er en sjømat som konsumeres over hele verden. Selv om reker og reker er i forskjellige underordner av Decapoda, er de veldig like i utseende og begrepene brukes ofte om hverandre i kommersielt oppdrett og i naturen."},
        {"Name": "Fisk","Del":3,"DivInformation":"FiskInfo","namm":"one","choseId":"Fiskidee", "iVerdi": 7, "LevId": "FiskAntal", "prisId1": "FiskPris","link":"images/middagsmeny/forrett/FiskBrod.jpg","butId": "bstFisk", "pris": 2, "idBox": "FiskBox","info":"Fisk er en god kilde til næringsstoffer som protein, vitamin B12, jod og selen. Fisk, spesielt de halvfete fiskene som rødspette, steinbit og kveite og fete fisker som laks, makrell, sild, ørret, ål, kveite og sardiner er hovedkilde til de marine omega-3 fettsyrene i kostholdet."},
        {"Name": "Plov","Del":4,"DivInformation":"PlovInfo","namm":"two","choseId":"Plovidee","iVerdi":8,"LevId":"PlovAntal","prisId1": "PlovPris","link": "images/middagsmeny/Hovedrett/Plov.jpg", "butId": "bstPlov", "pris": 10, "idBox": "PlovBox","info":"Ratatouille er en tradisjonell grønnsaksrett av provençalsk mat laget av pepper, aubergine og zucchini, på mange måter lik den ungarske lechoen."},
        {"Name": "Killing","Del":5,"DivInformation":"KillingInfo","namm":"two","choseId":"Killingidee", "iVerdi": 9, "LevId": "KillingAntal", "prisId1": "KillingPris","link":"images/middagsmeny/Hovedrett/kiling.jpg","butId": "bstKilling", "pris": 15, "idBox": "KillingBox","info":"det er en sjømat som konsumeres over hele verden. Selv om reker og reker er i forskjellige underordner av Decapoda, er de veldig like i utseende og begrepene brukes ofte om hverandre i kommersielt oppdrett og i naturen."},
        {"Name": "Fisk_og_Salat","Del":6,"DivInformation":"Fisk_og_SalatInfo","namm":"two","choseId":"Fisk_og_Salatidee", "iVerdi": 10, "LevId": "FiskSalatAntal", "prisId1": "FiskSalatPris","link":"images/middagsmeny/Hovedrett/fiskMedSalat.jpg","butId": "bstFiskSalat", "pris": 1200, "idBox": "FiskSalatBox","info":"Fisk er en god kilde til næringsstoffer som protein, vitamin B12, jod og selen. Fisk, spesielt de halvfete fiskene som rødspette, steinbit og kveite og fete fisker som laks, makrell, sild, ørret, ål, kveite og sardiner er hovedkilde til de marine omega-3 fettsyrene i kostholdet."},
        {"Name": "Pudding","Del":7,"DivInformation":"PuddingInfo","namm":"tree","choseId":"Puddingidee","iVerdi":11,"LevId":"PuddingAntal","prisId1": "PuddingPris","link": "images/middagsmeny/Deserts/Pudding.jpg", "butId": "bstPudding", "pris": 3, "idBox": "PuddingBox","info":"Ratatouille er en tradisjonell grønnsaksrett av provençalsk mat laget av pepper, aubergine og zucchini, på mange måter lik den ungarske lechoen."},
        {"Name": "Jogurt","Del":8,"DivInformation":"JogurtInfo","namm":"tree","choseId":"Jogurtidee", "iVerdi": 12, "LevId": "JogurtAntal", "prisId1": "JogurtPris","link":"images/middagsmeny/Deserts/Jogurt.jpg","butId": "bstJogurt", "pris": 3, "idBox": "JogurtBox","info":"det er en sjømat som konsumeres over hele verden. Selv om reker og reker er i forskjellige underordner av Decapoda, er de veldig like i utseende og begrepene brukes ofte om hverandre i kommersielt oppdrett og i naturen."},
        {"Name": "Kake","Del":9,"DivInformation":"KakeInfo","namm":"tree","choseId":"Kakeidee", "iVerdi": 13, "LevId": "KakeAntal", "prisId1": "KakePris","link":"images/middagsmeny/Deserts/Kake.png","butId": "bstKake", "pris": 17, "idBox": "KakeBox","info":"Fisk er en god kilde til næringsstoffer som protein, vitamin B12, jod og selen. Fisk, spesielt de halvfete fiskene som rødspette, steinbit og kveite og fete fisker som laks, makrell, sild, ørret, ål, kveite og sardiner er hovedkilde til de marine omega-3 fettsyrene i kostholdet."},
    ]
    return render(request, 'Middagsmeny.html',{"Masiv":masiven})


def tilbakeMening(request):
    masiven1=[
        {"Name": "Rødvin", "choseId": "Rødvin", "iVerdi": 14, "LevId": "RødvinAntal", "prisId1": "RødvinPris",
        "link": "images/drikke/vin/Rødvin.jpg", "butId": "bstRødvin", "pris": 5, "idBox": "RødvinBox",
        "info": "Ganske greit Rødvin"},
        {"Name": "Hvitvin", "choseId": "Hvitvin", "iVerdi": 15, "LevId": "HvitvinAntal", "prisId1": "HvitvinPris",
        "link": "images/drikke/vin/Hvitvin.jpg", "butId": "bstHvitvin", "pris": 8, "idBox": "HvitvinBox",
        "info": "Vanlig Vin"},
        {"Name": "Musserende_vin", "choseId": "Musserende_vin", "iVerdi": 16, "LevId": "Musserende_vinAntal", "prisId1": "Musserende_vinPris",
        "link": "images/drikke/vin/Musserende_vin.jpg", "butId": "bstMusserende_vin", "pris": 10, "idBox": "Musserende_vinBox",
        "info": "Vanlig Musserende_vin"},
        ]
    masiven2=[
        {"Name": "Lys Øl", "choseId": "Lys_Ol", "iVerdi": 17, "LevId": "Lys_OlAntal", "prisId1": "Lys_OlPris",
        "link": "images/middagsmeny/forrett/FiskBrod.jpg", "butId": "bstLys_Ol", "pris": 9, "idBox": "Lys_OlBox",
        "info": "Lys_Ol"},
        {"Name": "Hvitvin", "choseId": "Vin", "iVerdi": 18, "LevId": "VinAntal", "prisId1": "VinPris",
        "link": "images/middagsmeny/forrett/FiskBrod.jpg", "butId": "bstVin", "pris": 5, "idBox": "VinBox",
        "info": "Vanlig Vin"},
        {"Name": "Musserende vin", "choseId": "Vin", "iVerdi": 19, "LevId": "VinAntal", "prisId1": "VinPris",
        "link": "images/middagsmeny/forrett/FiskBrod.jpg", "butId": "bstVin", "pris": 5, "idBox": "VinBox",
        "info": "Vanlig Vin"},
        ]
    masiven3=[
        {"Name": "Rødvin", "choseId": "Vin", "iVerdi": 20, "LevId": "VinAntal", "prisId1": "VinPris",
        "link": "images/middagsmeny/forrett/FiskBrod.jpg", "butId": "bstVin", "pris": 5, "idBox": "VinBox",
        "info": "Vanlig Vin"},
        {"Name": "Hvitvin", "choseId": "Vin", "iVerdi": 21, "LevId": "VinAntal", "prisId1": "VinPris",
        "link": "images/middagsmeny/forrett/FiskBrod.jpg", "butId": "bstVin", "pris": 5, "idBox": "VinBox",
        "info": "Vanlig Vin"},
        {"Name": "Musserende vin", "choseId": "Vin", "iVerdi": 21, "LevId": "VinAntal", "prisId1": "VinPris",
        "link": "images/middagsmeny/forrett/FiskBrod.jpg", "butId": "bstVin", "pris": 5, "idBox": "VinBox",
        "info": "Vanlig Vin"},
        ]
        #{"Name": "Кeker", "Del": 2, "DivInformation": "КekerInfo", "namm": "one", "choseId": "Кekeridee", "iVerdi": 15,
        #"LevId": "КekerAntal", "prisId1": "КekerPris", "link": "images/middagsmeny/forrett/krevetki.jpg",
        #"butId": "bstКeker", "pris": 5, "idBox": "КekerBox",
        #"info": "det er en sjømat som konsumeres over hele verden. Selv om reker og reker er i forskjellige underordner av Decapoda, er de veldig like i utseende og begrepene brukes ofte om hverandre i kommersielt oppdrett og i naturen."},

    antal=[
        {"Id":"div1","Name":"Vin"},
        {"Id":"div2","Name":"Øl"},
        {"Id":"div3","Name":"MineralVann"},
        ]
    return render(request, 'Drikkemeny.html',{"Masiv1":masiven1,"Masiv2":masiven2,"Masiv3":masiven3,"AntalDiver":antal})

def Bordbestilling(request):
    print (request)
    return render(request, 'Bordbestilling.html',)
