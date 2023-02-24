print("----------Tuplas----------")
tupla_principal=(1,'Benjamin',10.90)#el string imprimirá entre comillas simples independiente si está escrita con dobles
print("Las tuplas pueden contener de todo: ")
print("tupla principal: ",tupla_principal)

tupla=(1,2,3,4)
print("Tupla: ",tupla)
print("El segundo valor de la tupla es: ",tupla[1])#se cuenta desde el 0
#tupla[0]=100 esto no funciona debido a que los valores de las tuplas no pueden ser modificados
print("")
tupla_1=(11,22,33,44)
tupla_2=(55,66,77,88)
tupla_3=tupla_1+tupla_2
print("El valor de las dos tuplas es: ",tupla_3,". Exito!!!")
print("")
tupla_repetidos=(1,4,3,4,5,6,6,6,34,4,2,4,4,5,7,5,7)
print("Tupla Repetidos: ",tupla_repetidos)
print("Tuplas repetidas: El numero 4 aparece ",tupla_repetidos.count(4)," veces!!!")

print("El numero 100 se encuentra en las tuplas repetidas?",100 in tupla_repetidos)
print("El numero 4 se encuentra en las tuplas repetidas?",4 in tupla_repetidos)

print("")