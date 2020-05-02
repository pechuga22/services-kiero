// const numero_alumnos=parseInt(prompt("Ingrese Numero de alumnos"));
// var cantm = 0, canth = 0, sumam = 0, sumah = 0
// let i=0
// while(i<numero_alumnos){
//     let choose=parseInt(prompt("Ingrese 1 si es hombre o 2 si es mujer"));
//     let age = parseInt(prompt("Ingrese edad: "));
//     if(choose === 1){
//         sumah =sumah+ age;
//         canth ++;
//     } else {
//        sumam = sumam + age;
//        cantm++;
//     }
//     console.log(sumah)
//     console.log(sumam)
//     i++;
// }
// const ph = sumah / canth;
// const pm = sumam / cantm;
// const pt = (sumah + sumam) / numero_alumnos;
// setTimeout(() => {
//     console.log("porcentaje hombres", ph)
//     console.log("porcentaje mujeres", pm)
//     console.log("porcentaje total", pt)
// },5000)

//------------------------------------------------------------------------------------------

const numeros = parseInt(prompt("Ingrese cantidad de numeros"))
let i =0, menor=0
while (i < numeros){
    let num = parseInt(prompt("Ingrese numeros")); 
    if(i==1){
        menor = num
    }
   else{
     if(num < menor){
        menor = num
    }
   }
    i++
}
console.log('El numero menor es ', menor);


