// on va commenser par recuperer tout les element du dom

const touch = [...document.querySelectorAll('.buton')];

const listeKeycode = touch.map(touche => touche.dataset.key);

const ecran = document.querySelector(".ecran")

document.addEventListener('keydown',(e) => {
    const valeur = e.keyCode.toString()
    calculer(valeur)
})

document.addEventListener('click',(e) => {
    const valeur = e.target.dataset.key
     calculer(valeur)
 })

//  ecran.textContent = "0";
 
 const calculer = (valeur) => {
if(listeKeycode.includes(valeur)){
    switch(valeur){
        case '8':
            ecran.textContent = "";
            break;
        case '13':
            
            const calcul = eval(ecran.textContent)
            ecran.textContent = calcul
            break
        default:
            const indexKeycode = listeKeycode.indexOf(valeur)
            // if(valeur == '13'){
            //     ecran.textContent = "";
            // }
            const touche = touch[indexKeycode]  
            ecran.textContent+=touche.innerHTML      

    }
}
 }

 window.addEventListener('error',(e) => {

    alert('operation non pris en charge: ' + e.message)
 })