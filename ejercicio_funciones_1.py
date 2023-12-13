'''1. Crea una función para verificar si un número es par o impar y devuelva “El
número es par” o “El número es impar” según corresponda.
'''
def es_o_no_par(n):
  if n % 2==0:
    print(f'El número {n} es par')
  else:
    print(f'El número {n} es impar')

es_o_no_par(4)
'''Crea una función a la que pases un número como argumento, calcule el factorial
de ese número y haga print del resultado.
'''
def fact(n):
  factorial=1
  for i in range (1,n+1):
    factorial=factorial*i
  return(factorial)

fact(4)
print(f'El factorial del número es {fact(4)}')

'''Crea una función a la que se le pase un número como argumento, calcule la
cantidad de dígitos y haga print de “La cantidad de dígitos es:” y el resultado
total de dígitos.
PISTA: Para convertir un número a string usa el método str(). Te recordamos que
para saber la longitud de una cadena utilizamos len()
'''
'''
def contar_digitos(n):
  num_dig=len(str(n))
  print (f'Este número tiene {num_dig} dígitos')

n=input('Ingresa un número: ')
contar_digitos(n)
'''

'''1. Crea una función que, dado un número, sume los dígitos de ese número y
devuelva el resultado.
'''
def sumar_digitos(n): 
  suma = 0 
  while n > 0: 
    suma= suma+(n % 10)  
    n=n//10
  print('La suma de los números es: ', suma)

a=int(input('Ingrese un número: '))
sumar_digitos(a)

'''Dados dos números, crea una función para encontrar el mínimo común múltiplo
(MCM) de los dos números, que se les pasarán como argumento a la función, y
devuelva el MCM.
'''
'''Crea una función que, dada una palabra, cuente la cantidad de letras en una
palabra.
'''
def contar_letras (palabra):
  a=len(palabra)
  print(a)
contar_letras('lechuga')
''' Crea una función que, dada una lista de números, convierta la lista de números
a su valor absoluto.'''
def valor_abs(lista_numeros):
  for numero in lista_numeros:
    if numero >0:
      return (numero)
    else:
      return(abs(numero))
mi_lista=[5,-7,-15,3]
print(valor_abs(mi_lista))


