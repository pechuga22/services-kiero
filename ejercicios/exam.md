
<!-- inicio algoritmo -->
entero  cantidad_autos

escriba("Ingrese cantidad de autos")
lea cantidad_autos

calcular(cantidad_autos)


subproceso calcular(cantidad_autos)
entero amarillo, rosa, roja, azul, verde , ultimo_digito, i = 0
    mientras i < cantidad_autos haga
        escriba("Ingrese ultimo digito")
        lea ultimo_digito

        si ultimo_digito == 1 || ultimo digito == 2 entonces
            amarillo += 1
        sino
            si ultimo digito == 3 || ultimo_digito == 4 entonces
                rosa += 1
            sino
                si ultimo_digito ==5 || ultimo_digito == 6 entonces
                    roja += 1
                sino
                    si ultimo_digito == 7 || ultimo_digito == 8 entonces 
                        azul += 1
                    sino 
                        si ultimo_digito ==9 || ultimo_digito == 0 entonces 
                            verde += 1
                        finsi
                    finsi  
                finsi
            finsi
        finsi

        i ++
        fin mientras

imprima ("la cantidad de carros con calcomania  de color amarillo son" , amarillo) 
imprima ("la cantidad de carros con calcomania  de color rosa son" , rosa)        
imprima ("la cantidad de carros con calcomania  de color roja son" , roja)        
imprima ("la cantidad de carros con calcomania  de color azul son" , azul)        
imprima ("la cantidad de carros con calcomania  de color verde son" , verde)    

fin subproceso

                     
<!-- fin algoritmo -->







"ingrese numero 1"
leer numero_1
"ingrese numero 2"
leer numero_2


subproceso calculadora(numero_2, numero_1){
    entero respuesta = 0
    "Ingrese digito dependediendo del resul;tado que quiera: 1 para sumar, 2 para restar, 3 para multiplicar, 5 para dividir"
    lea digito

    switch(digito){
        case 1: digito == 1
    }
    respuesta = numero_2 + numero_1
    respuesta = numero_2 - numero_1
    respuesta = numero_2 * numero_1
    respuesta = numero_2 / numero_1

}



import java.util *;

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        for(int i = 0; i < 5; i++){
          System.out.println("Ingrese un numero: ");
          int num = sc.nextInt();

          if(i == num){
              menor = num
          } else{
              if (num < menor) {
                  menor = num
              }
          }

        }
    }
}


int i = 0
while i < 100














