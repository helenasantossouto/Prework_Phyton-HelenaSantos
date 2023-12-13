'''
Bucles
1. Ejercicio: Imprime los números del 1 al 10 usando un bucle for .
2. Ejercicio: Imprime los números pares del 1 al 20 usando un bucle while .
3. Ejercicio: Usa un bucle para calcular la suma de los números del 1 al 100.
'''
#1
for i in range (10):
  i=i
  print(i+1)
#2
x=1
while x<21:
  if x%2==0:
    print(x)
  x+=1
#3
lista_100=range(0,101,1)
suma=0
for numero in lista_100:
  suma=suma+numero
print(suma)
#
x=1
suma=0
while x<=100:
  suma=suma+x
  x+=1
print(suma)