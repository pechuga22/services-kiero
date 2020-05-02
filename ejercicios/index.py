# numero_alumnos=int(input("Ingrese Numero de alumnos: "))
# i = canth = cantm = sumah = sumam=0

# for i in range(0, numero_alumnos):
#     choose=int(input("Ingrese 1 si es hombre o 2 si es mujer: "))
#     age = int(input("Ingrese edad: "))
#     if choose == 1:
#          sumah +=age
#          canth +=1
#     else:
#         sumam += age
#         cantm += 1

# ph = sumah / canth
# pm = sumam / cantm
# pt = (sumah + sumam) / numero_alumnos

# print("porcentaje hombres", ph)
# print("porcentaje mujeres", pm)
# print("porcentaje total", pt)

#--------------------------------------------------------------------------



# def num_menor(): 
#     numeros = int(input("Ingrese Cantidad de numeros: "));
#     menor=otra(numeros)
#     return ({ menor})      

# def calculos(i, num):
#     menor = 0
#     if(i == 1):
#         menor = num
#     elif num < menor:
#         menor = num        

# def otra(numeros):
#     i = 0
#     while i < numeros:
#         num = int(input("Ingrese numero: "))
#         calculos(i, num)
#         i+=1 

# num_menor()        
# cadena = str(input("Digite una palabra:  "))

# print(cadena)
# 
# 
#     

# cant_autos= int(input("Ingrese Cantidad de autos"))

# i=0
# while i<cant_autos: 
#     ultimo_digito = int(input("Ingrese ultimo digito de su carro"));
#     if ultimo_digito == 1 or ultimo_digito == 2:



# suma_pares = suma_impares = contador_impares  = sumatoria = promedio_impares = 0
# i = 1
# productoria = 1
# while i <= 20:
#     num=int(input("Ingrese numeros enteros: "))
#     if num % 2 == 0:
#         suma_pares += num
#     else:
#         suma_impares += num
#         contador_impares +=1
#     if i == 5:
#         if num > 0 and num % 2 == 0:
#             mensaje = ("El quinto numero ingresado es par positivo")
#     if i <= 10:
#         print("Entraaaa")
#         productoria = productoria * num 
#         print(productoria)
#     if i >= 10 :
#         print("Entraaaaaaaaaaa")
#         sumatoria+= num
#         print(sumatoria)
#     i+= 1   
# #------- Muestro data ----------------------------
# promedio_impares = suma_impares / contador_impares    
# if suma_impares > promedio_impares:
#     print("La suma de los impares es mayor que el promedio de los impares")
# else:
#     print("El promedio de los impares es mayor a la suma de los impares")    
# print(mensaje)
# print("La suma de los numeros pares es: ", suma_pares)   
# print("La productoria de los primeros 15 numeros es:", productoria)
# print("La sumatoria de los ultimos 10 numeros es :", sumatoria)




# i= 1

# while i <  5:
#     num = int(input("Ingrese Numero"))

#     positivos(num)
#     negativos(num)
#     neutros(num)

# i +=1



# def positivos(num):
#     if num > 0 :
#         positivos += 1
#     print(positivos)

# def negativos(num):
#     if num < 0 :
#         negativos += 1
#     print(negativos)  

# def neutros(num):
#     if num == 0 :
#         neutros +=1        
#     print(neutros)


# def muestre():
#     neutros()
#     negativos()
#     positivos()  

# muestre()
def saludo():
    names = []
    for i in range(5):
        name = input("Ingrese nombre")
        names.append(name)
    print(names)

saludo()