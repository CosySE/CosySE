#Realiza una función separar(lista) que tome una lista de números enteros y devuelva dos listas ordenadas.
#  La primera con los números pares y la segunda con los números impares. 
import random

def separaLista(lista_new):
    lista_pares =[]
    lista_impares=[]
    for pares in lista_new: #recorre la lista creada aleatoria
        if pares % 2 == 0: #preguntp si cada elemento de la lista es divisible por 2 
            lista_pares.append(pares)#agrego a la lista
            lista_pares.sort()
        else:#si no es divisible por dos agrego a la lista impar
            lista_impares.append(pares)
            lista_impares.sort()
    print(f'Lista de pares {lista_pares} lista de imapares {lista_impares}')#imprimo las dos listas


if __name__=='__main__':
#crear una lista aleatoria con numeros enteros
    lista_new =[random.randint(1,80) for i in range(8)]
    print(lista_new)
    separaLista(lista_new)