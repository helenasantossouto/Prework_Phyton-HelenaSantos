''' Crea una función que, dada una lista de números, convierta la lista de números
a su valor absoluto.'''
'''def valor_abs(lista_numeros):
  for numero in lista_numeros:
    if numero >0:
      print (numero)
    else:
      print(abs(numero))
mi_lista=[-3,-7,-15,3]
valor_abs(mi_lista)'''

'''Ejercicio: Define una función que tome un número y retorne una lista de sus
divisores.'''

def divisores(n):
  for i in range(1,n+1):
    if n % i ==0:
      print(i)

divisores(6)

