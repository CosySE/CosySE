#tuplas set
# import sys
# import timeit
# a = (1,2,3,4,'stop')
# b= tuple()
# x,t,y,z,d = a
# #print(len(a))
# b=(2,)
#print(b)
#midict= {a[0:3]:'primer',a[4]:'segundo'}
#print(midict)
#direccion_correo = input('Ingrese un correo : ')
#usuario,dominio = direccion_correo.split('@')
#print(f'su usuario es --{usuario}, su dominio es --{dominio}')
#lista =[1,2,3,4,5]
# print(sys.getsizeof(lista))
# print(sys.getsizeof(a))
# print(timeit.timeit(stmt='[1,2,3,4,5,6,7,8]',number=1000000))
# print(timeit.timeit(stmt='(1,2,3,4,5,6,7,8)',number=1000000))
#-----SETS------
# miset = {1,2,3,4}
# miset_2 = set('hello')
# miset_3 = {2,4,5,7}
# resultado = miset.union(miset_2)
# resultad_2 = miset.intersection(miset_3)

# print(resultado,resultad_2)

import csv
lista = []
with open('export.csv') as archivo:
    lectura = csv.reader(archivo,delimiter=';')
    for i in lectura:
        if i[2]=='':
            i.pop()
            lista.append(i)
    print(lista) 