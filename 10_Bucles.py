print(" ----------------------------------")
print("|         BUCLES FOR/WHILE         |")
print(" ----------------------------------")
print("")

print("----------For----------")
#for "variable" in "elemento iterable"
#objetos iterables: strings, listas, tuplas, etc.
print("Esto imprime el valor de X en un ciclo For desde 0 hasta 10: ")
for x in range(10):{#esto es igual a for(x=0;x<10;x++)
    print(x)
}#puede ir así o si las llaves

print("-----------------------------------------------------------------------")
print("Esto imprime el valor de X en un ciclo For desde 5 hasta 10: ")
for x in range(5,10):
    print(x)

print("-----------------------------------------------------------------------")
print("Este ciclo For imprimirá caracter por caracter la palabra HOLA")
for x in 'Hola':#Comillas doble o simples funcionan igual
    print(x)

print("-----------------------------------------------------------------------")
print("Este ciclo For imprimirá los valores dentro de la Lista: ")
lista=['n',1,100,True]
for x in lista:
    print(x)
print("")
print("")
print("---------------WHILE----------------")

print("Este ciclo While imprimirá el valor de X desde 0 hasta 10: ")
x=0
while x<10:
    print(x)
    x+=1#esto es x=x+1


print("")
#---------BREAK, CONTINUE, PASS----------
print("---------------Break-------------------")
for x in range(10):
    print(x)
    if(x==8):
        break
        print("Esto interrumpe el ciclo For")


print("")
print("--------------Continue-----------------")
for x in range(10):
    if x==0:
        continue#Con este comando no pasa por X=0
    valor=x*x
    print("Valor ",x,": ",valor)


print("")
print("-----------------Pass--------------------")
print("El pass sirve para dejar un ciclo(while) vacío para luego completarlo")
x=10

while x<10:
    pass#sirve para dejar el codigo incompleto y no detecte ningun error hasta que le demos información