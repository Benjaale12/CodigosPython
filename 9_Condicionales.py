print("-------Condicionales IF-------")
a=1
b=2
print("A= ",a,"B= ",b)
print("¿A y B son iguales?")
if(a==b):
    print("R: a=b")
else:
    print("R: Son diferentes")

print("--------IF Anidados--------")
a=1
b=2
c=3
if(a==b):
    if(b==c):
        print("a=b=c")
    else:
        print("a=b pero b y c son diferentes")
else:
    print("a y b son diferentes")


print("-------------Elif= Else if---------------")
a=1
print("A= ",a)
if a>0:
    print("A>0")
elif a<0:
    print("A<0")#Dada la condicion este no se imprime
else:
    print("A=0")#Dada la condicion esta tampoco se imprime
#En Python no se usa Switch/Case