'''
Condicionales
1. Ejercicio: Dado un número, imprime si es positivo o negativo.
2. Ejercicio: Dado un número, imprime si es par o impar.
3. Ejercicio: Dado tres números, encuentra y muestra el mayor de ellos.
'''
'''
#1
x=(input("Ingresa un número: "))
if x<0:
  print(f'El número {x} es un número es negativo')
else:
  print(f'El número {x} es un número positivo')
#2
numero = int(input("Ingresa un número: "))
if numero % 2 == 0:
    print("El número es par")
else:
    print("El número es impar")
'''

#3
n1=int(input('Ingrese el primer número: '))
n2=int(input('Ingrese el segundo número: '))
n3=int(input('Ingrese el tercer número: '))

numeros=[n1,n2,n3]
mayor=numeros[0]
for numero in numeros:
  if numero > mayor:
    mayor = numero
print(f'el número mayor es el {mayor}')
