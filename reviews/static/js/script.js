            let varene=[
        {"Name":"Burger","BtnMinId":"BurgerMinbtn" , "BtnMaxId":"BurgerMaxbtn", "butId":"bstBurger", "pris":5, "antal":"BurgerAntal","PrisId":"BurgerPris"},
        {"Name":"Buter","BtnMinId":"ButerMinbtn" , "BtnMaxId":"ButerMaxbtn", "butId":"bstButer", "pris":6.50, "antal":"ButerAntal","PrisId":"ButerPris"},
        {"Name":"Salat","BtnMinId":"SalatMinbtn" , "BtnMaxId":"SalatMaxbtn", "butId":"bstSalat", "pris":5.50, "antal":"SalatAntal","PrisId":"SalatPris"},
        {"Name":"Suppe","BtnMinId":"SuppeMinbtn" , "BtnMaxId":"SuppeMaxbtn", "butId":"bstSuppe", "pris":3, "antal":"SuppeAntal","PrisId":"SuppePris"},
        {"Name":"Grøt","BtnMinId":"GrøtMinbtn" , "BtnMaxId":"GrotMaxbtn", "butId":"bstKasja", "pris":2.50, "antal":"KasjaAntal","PrisId":"GrotPris"},
        {"Name":"Ratatouille","BtnMinId":"RatatouilleMinbtn" , "BtnMaxId":"RatatouilleMaxbtn", "pris":10, "butId":"bstRatatouille", "antal":"RatatouilleAntal","PrisId":"RatatouillePris"},
        {"Name":"Кeker","BtnMinId":"КekerMinbtn" , "BtnMaxId":"КekerMaxbtn", "butId":"bstКeker", "pris":5, "antal":"КekerAntal","PrisId":"КekerPris"},
        {"Name":"Fisk","BtnMinId":"FiskMinbtn" , "BtnMaxId":"FiskMaxbtn", "butId":"bstFisk", "pris":2, "antal":"FiskAntal","PrisId":"FiskPris"},
        {"Name":"Plov","BtnMinId":"PlovMinbtn" , "BtnMaxId":"PlovMaxbtn", "butId":"bstPlov", "pris":10, "antal":"PlovAntal","PrisId":"PlovPris"},
        {"Name":"Killing","BtnMinId":"KillingMinbtn" , "BtnMaxId":"KillingMaxbtn", "butId":"KillingFisk", "pris":15, "antal":"KillingAntal","PrisId":"KillingPris"},
        {"Name":"Fisk_og_Salat","BtnMinId":"FiskSalatMinbtn" , "BtnMaxId":"FiskSalatMaxbtn", "butId":"bstFiskSalat", "pris":1200, "antal":"FiskSalatAntal","PrisId":"FiskSalatPris"},
        {"Name":"Pudding","BtnMinId":"PuddingMinbtn" , "BtnMaxId":"PuddingMaxbtn", "butId":"bstPudding", "pris":3, "antal":"PuddingAntal","PrisId":"PuddingPris"},
        {"Name":"Jogurt","BtnMinId":"JogurtMinbtn" , "BtnMaxId":"JogurtMaxbtn", "butId":"bstJogurt", "pris":3, "antal":"JogurtAntal","PrisId":"JogurtPris"},
        {"Name":"Kake","BtnMinId":"KakeMinbtn" , "BtnMaxId":"KakeMaxbtn", "butId":"bstKake", "pris":17, "antal":"KakeAntal","PrisId":"KakePris"},
        {"Name":"Vin","BtnMinId":"VinMinbtn" , "BtnMaxId":"VinMaxbtn", "butId":"bstVin", "pris":5, "antal":"VinAntal","PrisId":"VinPris"},
        {"Name":"Hvitvin","BtnMinId":"HvitvinMinbtn" , "BtnMaxId":"HvitvinMaxbtn", "butId":"bstHvitvin", "pris":8, "antal":"HvitvinAntal","PrisId":"HvitvinPris"},
        {"Name":"Musserende vinn","BtnMinId":"MusserendeVinnMinbtn" , "BtnMaxId":"MusserendeVinnMaxbtn", "butId":"bstMusserendeVinn", "pris":10, "antal":"MusserendeVinnAntal","PrisId":"MusserendeVinnPris"},
        {"Name":"Lys Øl","BtnMinId":"LysOlMinbtn" , "BtnMaxId":"LysOlMaxbtn", "butId":"bstLysOl", "pris":7, "antal":"LysOlAntal","PrisId":"LysOlPris"},
        {"Name":"Pale Øl","BtnMinId":"PaleOlMinbtn" , "BtnMaxId":"PaleOlMaxbtn", "butId":"bstPaleOl", "pris":5, "antal":"PaleOlAntal","PrisId":"PaleOlPris"},
        {"Name":"Belgian Øl","BtnMinId":"BelgianOlMinbtn" , "BtnMaxId":"BelgianOlMaxbtn", "butId":"bstBelgianOl", "pris":2, "antal":"BelgianOlAntal","PrisId":"BelgianOlPris"},
        {"Name":"Vann","BtnMinId":"VannMinbtn" , "BtnMaxId":"VannMaxbtn", "butId":"bstVann", "pris":1, "antal":"VannAntal","PrisId":"VannPris"},
        {"Name":"Fanta","BtnMinId":"FantaMinbtn" , "BtnMaxId":"FantaMaxbtn", "butId":"bstFanta", "pris":2, "antal":"FantaAntal","PrisId":"FantaPris"},
        {"Name":"CocaCola","BtnMinId":"CocaColaMinbtn" , "BtnMaxId":"CocaColaMaxbtn", "butId":"bstCocaCola", "pris":2, "antal":"BelgianCocaCola","PrisId":"BelgianCocaCola"},
    ]

     let inf1=["RatatouilleInfo","КekerInfo","FiskInfo"]
     let inf2=["PlovInfo","KillingInfo","Fisk_og_SalatInfo"]
     let inf3=["PuddingInfo","JogurtInfo", "KakeInfo"]
     let middagsInfo=[inf1,inf2,inf3]

     let info1=["Ratatouilleidee","Кekeridee","Fiskidee"]
     let info2=["Plovidee","Killingidee","Fisk_og_Salatidee"]
     let info3=["Puddingidee","Jogurtidee","Kakeidee"]
     let middagsChoisId=[info1,info2,info3]

     let middagsmeny=["Forrett","Hovedrett","Dessert"]
     function visse(a)
     {

            document.getElementById(a).classList.toggle("lunchBlock2")
     }

    function ViseMidd(navnId)
    {
        for(let i=0;i<middagsmeny.length;i++)
        {
            if(middagsmeny[i]==navnId)
            {
                document.getElementById(navnId).style.display="flex"
            }
            else
            {
                document.getElementById(middagsmeny[i]).style.display="none"
            }
        }
    }

    function showDivInfo(Id, Id2, number)
    {
        for(let i=0;i<middagsChoisId.length;i++)
        {
            for(let g=0;g<middagsChoisId.length;g++)
            {
                if(Id2==info1[g])
                {
                    for(let f=0;f<info1.length;f++)
                    {
                        document.getElementById(middagsInfo[0][f]).style.display="none"
                    }
                        document.getElementById(Id).style.display="block"
                }
                if(Id2==info2[g])
                {
                    for(let f=0;f<info2.length;f++)
                    {
                        document.getElementById(middagsInfo[1][f]).style.display="none"
                    }
                        document.getElementById(Id).style.display="block"
                }
                if(Id2==info3[g])
                {
                    for(let f=0;f<info3.length;f++)
                    {
                        document.getElementById(middagsInfo[2][f]).style.display="none"
                    }
                        document.getElementById(Id).style.display="block"
                }
            }
        }

    }

/**************Kvitering*******************/
        /*
        let divMainEl=document.getElementById("scroll")
        for(var i=0;i<varene.length;i++)
        {
            let div2El=document.createElement("div")
            let divPMEl=document.createElement("div")
            let btnMinEl=document.createElement("input")
            btnMinEl.type = "button"
            btnMinEl.className="BtnMin"
            let pEl=document.createElement("p")
            let btnMerEl=document.createElement("input")
            btnMerEl.type = "button"
            btnMerEl.className="BtnPlus"
            let div3El=document.createElement("div")
            let p2El=document.createElement("p")
            let spanEl=document.createElement("span")
            let h4El=document.createElement("h4")
            div2El.id=varene[i]["Name"]
            div2El.className="KvitLi"
            h4El.innerHTML=varene[i]["Name"]
            div2El.appendChild(h4El)
            divPMEl.className="PlusMinus"
            btnMinEl.value="-"
            btnMinEl.id=varene[i]["BtnMinId"]
            pEl.id=varene[i]["antal"]
            pEl.value=0
            pEl.innerHTML="1"
            btnMerEl.value="+"
            btnMerEl.id=varene[i]["BtnMaxId"]
            divPMEl.appendChild(btnMinEl)
            divPMEl.appendChild(pEl)
            divPMEl.appendChild(btnMerEl)
            div2El.appendChild(divPMEl)
            div3El.className="KvitPris"
            p2El.innerHTML=varene[i]["pris"]+"€"
            p2El.id=varene[i]["PrisId"]
            p2El.value=varene[i]["pris"]
            spanEl.className="close"
            spanEl.id=varene[i]["Name"]+"Close"
            div3El.appendChild(p2El)
            div3El.appendChild(spanEl)
            div2El.appendChild(div3El)
            div2El.style.display="none"
            divMainEl.appendChild(div2El)
            ///////////////////////////////////
            let Antid=varene[i]["antal"]
            let blockId=varene[i]["Name"]
            let PrisId=varene[i]["PrisId"]
            let priss=varene[i]["pris"]
            let iVerdi=i
            document.getElementById(varene[i]["antal"]).innerHTML=0

            spanEl.addEventListener('click', function(){
            dalateElem(Antid,blockId,priss,iVerdi);
            });

            btnMinEl.addEventListener('click', function(){
            MinOnclick(Antid,blockId,priss,iVerdi,PrisId);
            });
            btnMerEl.addEventListener('click', function(){
            MaxOnclick(Antid,blockId,priss,iVerdi,PrisId);
            });
        }*/

    let summenAvVarene=0
    let summen=0
    let KvitNames=[]
    function CreateKvitEl(Antid,blockId, priss, iVerdi, prisId)
    {

        document.getElementById("varene").innerHTML=++summenAvVarene
        if(!KvitNames.includes(varene[iVerdi]["Name"]))
        {
            const shablon = document.querySelector("#Shablon").cloneNode(true)
            const scroll=document.querySelector("#scroll")
            const spanEl=shablon.querySelector("#ShablonClose")
            const nameEl=shablon.querySelector("h4")
            const btnMinEl=shablon.querySelector("#ShablonMinbtn")
            const btnMerEl=shablon.querySelector("#ShablonMaxbtn")
            const prisEl=shablon.querySelector("#ShablonPris")

            shablon.setAttribute("index",iVerdi)

            KvitNames.push(varene[iVerdi]["Name"])
            nameEl.innerHTML=varene[iVerdi]["Name"]
            prisEl.innerHTML=varene[iVerdi]["pris"]

            shablon.style.display="flex";
            scroll.appendChild(shablon)
            summen+=varene[iVerdi]["pris"]
            document.getElementById("KvitBigPris").innerHTML=summen+"€"

            spanEl.addEventListener('click', function(){
            dalateElem(shablon,iVerdi);
            });

            /*btnMerEl.addEventListener('click', function(){
            MaxOnclick(Antid,blockId,priss,iVerdi,prisId);
            });*/
            btnMerEl.addEventListener('click', function(){
                MaxOnclick(shablon,iVerdi)
            });

            btnMinEl.addEventListener('click', function(){
            MinOnclick(iVerdi);
            });

        }
        else
        {
            const selector ="[index='"+String(iVerdi)+"']"
            document.querySelector(selector).querySelector("#ShablonMaxbtn").click()

        }
    }

    function MaxOnclick(shablon,iVerdi)
    {

            shablon.querySelector("#ShablonAntal").innerHTML=String(Number(shablon.querySelector("#ShablonAntal").innerHTML)+1)
            shablon.querySelector("#ShablonPris").innerHTML=Number(shablon.querySelector("#ShablonAntal").innerHTML)*varene[iVerdi]["pris"]
            summen+=varene[iVerdi]["pris"]
            document.getElementById("KvitBigPris").innerHTML=summen+"€"

        /*summenAvVarene++
        antalVarene[iVerdi]+=1
        summen+=priss
        console.log(Antid,blockId, priss, iVerdi, prisId,summenAvVarene,summen)
        console.log(priss * antalVarene[iVerdi] +"€")
        document.getElementById(blockId).style.display="flex";
        document.getElementById(prisId).innerHTML=priss * antalVarene[iVerdi] +"€"
        document.getElementById(Antid).innerHTML=antalVarene[iVerdi]
        document.getElementById("KvitBigPris").innerHTML=summen+"€"
        document.getElementById("varene").innerHTML=summenAvVarene
*/

    }

    function MinOnclick(iVerdi)
    {
        console.log(1111111)
        const selector ="[index='"+String(iVerdi)+"']"
        const shablon=document.querySelector(selector)
        if(shablon)
        {
            shablon.querySelector("#ShablonAntal").innerHTML=String(Number(shablon.querySelector("#ShablonAntal").innerHTML)-1)
            shablon.querySelector("#ShablonPris").innerHTML=(Number(shablon.querySelector("#ShablonAntal").innerHTML)*varene[iVerdi]["pris"])+"€"
            summen-=varene[iVerdi]["pris"]
            document.getElementById("KvitBigPris").innerHTML=summen+"€"
            document.getElementById("varene").innerHTML=--summenAvVarene

            if(shablon.querySelector("#ShablonAntal").innerHTML==0)
            {
                KvitNames=KvitNames.filter((item)=>item!=shablon.querySelector("h4").innerHTML)
                shablon.remove()

            }
        }


    }

    function dalateElem(shablon,iVerdi)
    {
        summenAvVarene-=shablon.querySelector("#ShablonAntal").innerHTML
        summen-= (varene[iVerdi]["pris"]) * Number(shablon.querySelector("#ShablonAntal").innerHTML)
        shablon.querySelector("#ShablonAntal").innerHTML=0
        shablon.querySelector("#ShablonPris").innerHTML=0+"€"
        document.getElementById("KvitBigPris").innerHTML=summen+"€"
        document.getElementById("varene").innerHTML=summenAvVarene
        shablon.remove()
    }

    function visKvit()
    {
        document.getElementById("KvitBack").style.display="block"
        document.getElementById("wolf").style.overflow="hidden"

    }
    /*Knappene i Kvitering*/
    function kvitering()
    {
        if(summen!=0)
        {
            if(confirm("Er du sikert at du vil betale?")==true)
            {
                location.reload();
            }
        }
        else
        {
            alert("Du har ikke noe i kurven")
        }

    }

    function Tilbake()
    {
        document.getElementById("KvitBack").style.display="none"
        document.getElementById("wolf").style.overflow="visible"

    }
    function allLegeUt()
    {
        let a=0
        const mainEl=document.querySelector("#scroll")
        mainEl.querySelectorAll(".KvitLi").forEach((item)=>{

            if(a>0)
            {
                summenAvVarene=0
                summen=0
                item.querySelector("#ShablonAntal").innerHTML=0
                item.querySelector("#ShablonPris").innerHTML=0
                document.getElementById("KvitBigPris").innerHTML=summen+"€"
                document.getElementById("varene").innerHTML=summenAvVarene
                KvitNames=KvitNames.filter((item2)=>item2!=item.querySelector("h4").innerHTML)
                item.remove()
            }
        a++
        })

    }
    /*********drikkemeny************/

        const alledrikkene=document.querySelectorAll(".radio")
        alledrikkene.forEach((item)=>{
        item.onclick=()=>{
        alledrikkene.forEach((item)=>{
            let block=document.getElementById(item.id.replace("_block",""))
            block.style.display="none"
        })
        let block=document.getElementById(item.id.replace("_block",""))
        bindFilter(block)
        block.style.display="block"


        }
    })

    function bindFilter(block)
    {

        const select=block.querySelector(".selectDrikker")
        console.log(select)
        select.addEventListener("change",(value)=>{
        console.log(select.value)
        block.querySelectorAll(".middMatt").forEach((item)=>{

            if(select.value=="all")
            {
                item.style.display="block"
                block.querySelector(".wrapper").classList.remove("wrapper_one")
            }
            else
            {
            block.querySelector(".wrapper").classList.add("wrapper_one")
            if(item.id!=select.value)
            {item.style.display="none"}
            else
            {item.style.display="block"}
            }

        })
    })
    }




    /*******************Tables****************/
     const tables = document.querySelectorAll(".tabel")
     tables.forEach((table)=>{
        table.onclick=()=>{
        document.getElementById("Tnumber").value=table.id.replace("stol","")
        }
     });
    document.querySelector("form").onsubmit=(e)=>{e.preventDefault(); alert(document.querySelector(".Tnumber1").value+" your table is "+ document.querySelector("#Tnumber").value)}



