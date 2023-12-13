'''
1. Ejercicio: Define una función que tome dos números y retorne su suma.
2. Ejercicio: Defineuna función que tome un número y retorne su factorial.
3. Ejercicio: Define una función que tome un número y determine si es primo.
4. Ejercicio: Define una función que reciba una lista de números y retorne la suma
de ellos.
5. Ejercicio: Define una función que reciba una cadena de texto y retorne la
cadena en reversa.
'''
#1
def suma(lista_numeros):
  suma=0
  for numero in lista_numeros:
    suma=suma+numero
  print(suma)

mi_lista=[2,4,7,8]
suma(mi_lista)

#1 variante
def suma_1 (a,b):
  la_suma=a+b
  print(la_suma)

suma_1(3,4)

#2
def funcion_factorial (n):
  fact=1
  for i in range(1,n+1):
    resultado=fact*i
  return(resultado)
funcion_factorial(4)
print(funcion_factorial(4))

#3
def primo(n):
  for num in range(2,n+1):
    if n % num ==0:
      return False
  return True
print(primo(6))

#4
def vuelta (cadena_texto):
  cadena_invertida= cadena_texto[::-1]
  print(cadena_invertida)

vuelta('Hola')