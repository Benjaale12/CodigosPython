print("--------Listas----------")
#las lista son muy parecidas a las tuplas pero los valores de las lista pueden ser cambiadas

lista_number_1=[1,'jose',90.9]
print("Lista 1: ",lista_number_1)

print("")
print("Aqui agregamos valores a una lista vacía, se suman por turno: ")
#Con append podemos agregar elementos, en este caso a una lista vacía
lista_number_2=[]#Esta es una lista vacía
lista_number_2.append(1)
print("Lista 2(append): ",lista_number_2)
lista_number_2.append(44)#Los valores se agregan en orden, el valor 1 va en la pos. [0] y el valor 44 en la pos.[1]
print("Lista 2(append): ",lista_number_2)

#print elementos de una lista en un for
print("")
lista_number_3=[1,2,3,'m',90.8,'Mario_bros']
print("For in lista 3: ")
for e in lista_number_3:#'e' son los elementos del for, es como la 'i' en .C
    print("Valor en for lista 3: ",e)

print("")
#aquí reemplazamos el 3er valor de lista_number_3 por"1000"
print("Reemplazo de un elemento de la lista: ")
lista_number_3[2]=1000#cambiamos el tercer valor
print("Lista 3: ",lista_number_3)

print("")
#concatenar listas
lista_conca_A=[1,2,3]
print("A=",lista_conca_A)
lista_conca_B=[4,5,6]
print("B=",lista_conca_B)
lista_conca_A+=lista_conca_B #Es lo mismo que decir       lista_conca_A=lista_conca_A + lista_conca_B
print("Suma de listas A y B: ",lista_conca_A)

print("")
#Append lista:
lista_append_1=[1,2,3]
lista_append_2=[4,5,6]
lista_append_1.append(lista_append_2)
print("Append listas:(una lista dentro de una lista)",lista_append_1)# += no es lo mismo que append

print("")
#insert, agregamos un elemento en una posición especifica
lista_insert=[11,22,33]
print("Lista insert, aquí cambiaremos el elemento de una posición especifica: ",lista_insert)
lista_insert.insert(0,'m')
print("La primera posición fue agregada por una M: ",lista_insert)#Agregamos un elemento(m) en una posición especifica, aumentan los elementos

lista_insert=[1,2,3]
print("Lista insert, aquí agregaremos un elemento en una posición especifica: ",lista_insert)
lista_insert.insert(10,'m')
print("La posicion 10 fue agregada con una M, pero...: ",lista_insert)#Agregamos un elemento(m) en una posición especifica, aumentan los elementos
#La posicion 10 no existe así que el elemento M será agregado en la ultima posición

print("------Lista 2da parte------")
print("Del en una lista: ")
#con esto borramos o eliminamos un elemento
listaA=[1,2,3]
print("Lista DEL SIN BORRAR nada: ",listaA)
del(listaA[2])
print("Lista luego de BORRAR: ",listaA)

print("")
lista_remov=[1,2,3,2,4,5]
print("Remove en una lista: ")
print("Lista SIN REMOVER: ",lista_remov)
lista_remov.remove(2)
print("Lista luego de REMOVER: ",lista_remov)
print("-Se eliminó el primer '2' de la lista!!!")

print("")
print("Lista Pop() quita un elemento: ")
list_pop=[1,2,3,2,4,5]
print("Lista sin popear: ",list_pop)
list_pop.pop()
print("Lista despues de Popear: ",list_pop)
print("")

print("Lista Pop(2) quita un elemento: ")
list_pop=[1,2,3,2,4,5]
print("Lista sin popear: ",list_pop)
list_pop.pop(2)#esto elimina el 3er elemento de la lista(0,1,2)
print("Lista despues de Popear: ",list_pop)
print("")

print("Sort en una lista:")
lista_sort_A=[1,2,3,2,4,5]
print("Lista antes del comando Sort: ",lista_sort_A)
lista_sort_A.sort()#Esto ordena los valores de la lista de menor a mayor
print("Lista despues del comando Sort: ",lista_sort_A)
lista_sort_A.sort(reverse=True)#Esto ordena los valores de la lista de mayor a menor
print("Lista despues del comando Sort reverse: ",lista_sort_A)
print("")
