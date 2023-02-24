print("------Diccionarios-------")
dicc={"nombre":"jose","apellido":"ramos","edad":28}#Los diccionarios usan llaves

#diccionario={key:valor,key:valor,key:valor}, Los caracteres y strings van entre comillas dobles y los numeros NO.
#Incluso podría ser dicc={28:"edad"}

print("Diccionario original: ",dicc)
dicc["apellido"]="lopez"
print("Diccionario despues de modificar el apellido",dicc)

print("")
#Metodos de un diccionario
print("Imprimir solo las KEYS: ",dicc.keys())#Esto solo imprime las keys, osea sin valores
print("Imprimir ITEMS: ",dicc.items())#acceso a las keys y los valores
print("Imprimir VALORES: ",dicc.values())#Solo imprime los valores de las llaves

print("")
#Eliminar y agregar elementos
dicc={"nombre":"jose","apellido":"ramos","edad":28}
print("Diccionario original: ",dicc)
del(dicc['nombre'])#Esto elimina la KEY y el VALOR de del DICCIONARIO
print("Imprimir con DEL: ",dicc.values())
#print(dicc)

print("")
dicc={"nombre":"jose","apellido":"ramos","edad":28}
print("Diccionario original: ",dicc)
dicc['x']=100#Esto agrega un KEY y un Valor al final del Diccionario
#si la key X ya existía entonces en vez de agregar una key al final, esta se modifica
print("Imprimir despues de agregar X=100: ",dicc.values())
#print(dicc)

