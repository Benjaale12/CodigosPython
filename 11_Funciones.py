print("------------Funcion------------")

def saludar():#Aqui se define la funcion
    print("buenos dias")

saludar()#aquí se hace llamado a la funcion

print("")
print("----------Funciones con parametros-----------")
def saludar(nombre,edad,pais):
    #print("Buenos dias"+nombre)
    print("Buenos dias ",nombre ," de ", edad ," años")
    print("Pais: "+pais)


saludar("Benjamin","23","chile")


print("")
print("------------Retorno de valores en funciones-------------")
def saludar(nombre):

    return "buenos dias "+nombre
x=saludar("Jose")
#Estos dos de abajo imprimen lo mismo
print(x)
print(saludar("Jose"))

def suma(hola):
    return 1+1

x=suma("cualquier_cosa")
print("Esto debe retornar la suma de 1+1: ",x)


print("")
print("-----------Parametros con valor por defecto----------")

def saludar(x,nombre="Jose"):#Si no pongo una variable para nombre este por defecto será Jose
    print("buenos dias "+nombre)

saludar(1)#es obligacion poner una variable "nombre" o dará error
saludar(1,"Antony")#Aqui por defecto es Jose pero como declaramos el string nombre=Antony saludará el antony y no a jose



print("")
print("-------------Parametros con nombre-------------")
def saludar(x,nombre):
    print("x= ",x)
    print("Buenos dias "+nombre)

saludar(x=1, nombre="jose")
saludar(nombre="jose",x=1)#da lo mismo el orden siempre y cuando se escriba de esta manera el llamado a la funcion ej: x=1


print("")
print("-------Funciones con diferente cantidad de parametros--------")
def saludar(x,*numeros):#esta funcion dice que tiene que ser al menos 2 parametros
    for n in numeros:
        print(n)
saludar(1,2,3)#1 pasa por la variable X y 2,3 pasan por la variable numeros
saludar(1,1,2,3,4,5,6,7,8,9,10)#numeros pasa a tomar desde la 2da variable hasta la ultima que haya
print("Si no le damos ningun valor a *numero imprimirá: ")
saludar(1)#esto no imprimirá nada ya que no hay valor y ademas no dará error, a diferencia de la variable X que si causa conflicto