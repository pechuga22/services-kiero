import java.util *;

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        while(i <= 100){
            System.out.println("Ingrese numeros enteros");
            int num = sc.nextInt();
            if(num % 2 == 0){
                suma_pares += num;
            } else {
                suma_impares += num;
                contador_impares += 1;
            }
            if(i == 5){
                if(num > 0 && num % 2 == 0){
                    mensaje = "El quinto numero ingresado es par positivo"
                }
            }
            if(i<=15){
                productoria *= num
            }
            if(i >= 90){
                sumatoria += num
            }
          i++  
        }
        promedio_impares = suma_impares / contador_impares;    
        if(suma_impares > promedio_impares){
            System.out.println("La suma de los impares es mayor que el promedio de los impares");
        } else{
            System.out.println("El promedio de los impares es mayor a la suma de los impares");
        }
        System.out.println(mensaje)
        System.out.println("La suma de los numeros pares es: ", suma_pares);
        System.out.println("La productoria de los primeros 15 numeros es: ", productoria);
        System.out.println("La sumatoria de los ultimos 10 numeros es: ", sumatoria)
    }
}

// suma_pares = suma_impares = contador_impares  = sumatoria = promedio_impares = 0
// i = 1
// productoria = 1
// while i <= 20:
//     num=int(input("Ingrese numeros enteros: "))
//     if num % 2 == 0:
//         suma_pares += num
//     else:
//         suma_impares += num
//         contador_impares +=1
//     if i == 5:
//         if num > 0 and num % 2 == 0:
//             mensaje = ("El quinto numero ingresado es par positivo")
//     if i <= 10:
//         print("Entraaaa")
//         productoria = productoria * num 
//         print(productoria)
//     if i >= 10 :
//         print("Entraaaaaaaaaaa")
//         sumatoria+= num
//         print(sumatoria)
//     i+= 1   
// #------- Muestro data ----------------------------
// promedio_impares = suma_impares / contador_impares    
// if suma_impares > promedio_impares:
//     print("La suma de los impares es mayor que el promedio de los impares")
// else:
//     print("El promedio de los impares es mayor a la suma de los impares")    
// print(mensaje)
// print("La suma de los numeros pares es: ", suma_pares)   
// print("La productoria de los primeros 15 numeros es:", productoria)
// print("La sumatoria de los ultimos 10 numeros es :", sumatoria)






