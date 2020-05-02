// // Este codigo ha sido generado por el modulo psexport 20180802-l64 de PSeInt.
// // Es posible que el codigo generado no sea completamente correcto. Si encuentra
// // errores por favor reportelos en el foro (http://pseint.sourceforge.net).

// function sin_titulo() {
// 	var cantidad_autos;
// 	document.write(("Ingrese cantidad de autos"),'<BR/>');
// 	cantidad_autos = prompt();
// 	calcular(cantidad_autos);
// }


// recive_Data(() => {
// 	console.log('click')
// })


// recibirData(data), () => {
// 	let saludo = "Hola";
// 	function saludar(saludo) {

// 	}
// }

// calcular(cantidad_autos), () => {

// 	var amarillo, azul, i, roja, rosa, ultimo_digito, verde;
// 	while (i<cantidad_autos) {
// 		document.write(("Ingrese ultimo digito"),'<BR/>');
// 		ultimo_digito = prompt();
// 		if (ultimo_digito==1 || ultimo_digito==2) {
// 			amarillo = amarillo+1;
// 		} else {
// 			if (ultimo_digito==3 || ultimo_digito==4) {
// 				rosa = rosa+1;
// 			} else {
// 				if (ultimo_digito==5 || ultimo_digito==6) {
// 					roja = roja+1;
// 				} else {
// 					if (ultimo_digito==7 || ultimo_digito==8) {
// 						azul = azul+1;
// 					} else {
// 						if (ultimo_digito==9 || ultimo_digito==0) {
// 							verde = verde+1;
// 						}
// 					}
// 				}
// 			}
// 		}
// 		i = i+1;
	
// 	document.write((amarillo),'<BR/>');
// 	document.write((rosa),'<BR/>');
// 	document.write((roja),'<BR/>');
// 	document.write((azul),'<BR/>');
// 	document.write((verde),'<BR/>');
// }
// }


// sett

// Console.LOG(DIO)
// setTimeout(() => {
// 	console.log("Ey, numero uno, dar las gracias ")
// },3000)
// setTimeout(() => {
// 	console.log("camina mirando para arriba, no con arrogancia ")
// },5000)
// setTimeout(() => {
// 	console.log("ey, divisando todo la galaxia ")
// },7000)
// setTimeout(() => {
// 	console.log("gracias por hacer de mi una liendra, que elegancia ") 
// },9000)
// setTimeout(() => {
// 	console.log("Ey, cambia el flow para que se inquiete")
// },12000)
// setTimeout(() => {
// 	console.log("no hay que ser un propio pa tener un Huete ")
// },15000)
// setTimeout(() => {
// 	console.log("no hay que ser galán, para tener par de fletes")
	
// },17000)
// setTimeout(() => {
// 	console.log("que se escuche la voz, para que respete")
// },19000)
// setTimeout(() => {
// 	console.log("jaa esto se trata se sonreir")
// },21000)

// const calculate = ({price, discount}) => {
// 	 return price - discount * price
// }

// const payments = calculate(100, 0.1)
// console.log(payments)


// const numerosPositivos=(num)=>{
// }

// const numerosNegativos = (num) => {
// }

// const numerosNeutros = (num) => {
// }

const calculos = () => {
	let cantidadNumeros = parseInt(prompt("Ingrese cantidad de numeros"))
	cantidadNumeros.map(num => num > 0 ? numeros_positivos += 1 : num < 0 ? numeros_negativos += 1 : num == 0 ? numeros_neutros += 1: "")
	data(numeros_positivos,numeros_negativos,numeros_neutros)
}
const data = (positivos, negativos, neutros) =>{
	console.log("Positivos: ", positivos, " Negativos: ", negativos, " Neutros: ", neutros);
}
calculos()


