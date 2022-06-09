from ast import Lambda


def suma(a,b):
    return a+b

print(suma(4,5))

# # lambda parametros : expresion 
# sumando = lambda a,b : a+b

# print(sumando(6,1))
a= ['x','d',3,5]
construir= lambda lista: lista[1] + 'ia'

print(construir(a))
#filter
#filter(condicional,coleccion de datos)
lista = [21,5,10,4,25,40]

def multiplo(valores):
    if valores % 5 ==0:
        return True

print(list(filter(multiplo,lista)))

print(list(filter(lambda lista: lista>10,lista)))