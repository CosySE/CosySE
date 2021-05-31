# vamos a estar viendo en esta clase tipos de datos listas , tuplas ,diccionarios ,set
#que es un funcion, condicionales en una funcion 
#try except para evitar salir del programa 
# las cadenas son secuencias de caracteres , no se pueden modificar pero si los puedes 
#comparar ,buscar en ellos contar etc
# listas son elementos mutables , se pueden ordenar y duplicar

# fruta  =  'platano'
# print(type(fruta))
# print('a' in fruta)# aqui le deciros esta la letra a en la cadena
# print ('z' in fruta)
# print(dir(fruta))
# print(f' Ponme la cadena con la primera letra en mayuscula {fruta.capitalize()}')
# print(f' Ponme todo en mayuscula {fruta.upper()}')
# print(len(fruta))# la cantiddd de elementos de la cadena

# lista = [2,5,6,8,7,4,4]
# print (lista)
# lista_dos = [2] * 5
# print(lista_dos)
# print (lista + lista_dos)
# casa = list()
# print(casa)
# casa.append('playa')
# casa.append('cerro')
# casa.append('miramar')# 
# print(casa)
# otra  =  casa.sort()
# print(otra)#La mayoría de métodos no regresan nada; modifican la lista y regresan None. Si
#accidentalmentes escribes print(otra)como yo  vas a decepcionarte con el resultado.
# pero ya esta ordenada
#print(casa)
# eliminar .pop
#print(len(lista))# la funcion len te cuenta los elementos de tu lista y cadena empezando por uno pero si vas a referirte
#algun elemento ene especifico debes hacerlo recordando que empiezan en cero
#lista.pop(6)
# print (lista)
# print(lista[2:])# muestra desde el elemento dos hasta el final
# print(lista[:])# completa
# print(lista[0:5])#desde el principio hasta el elemento 5 y no lo incluye imporante  
# # cada una de las funciones que tiene la lista la pueden ir probando por su cuenta solo queria mostrarles una parte
# las listas se pueden copiar 
# casa_copia  = casa
# print(casa_copia)
# casa_copia.pop(-1)
# print(casa_copia,casa)
# casa_copia = casa.copy()
# casa_copia.append('san miguel')
# print(casa_copia,casa)
# diccionarios son muy parecido a las listas ya que son mutables pero no esta ordenado precisamente tiene pares de valores ordenado en clae y valor 
#cada llave o clave a punta a un valor 
midict = {}
diccionario = dict()
diccionario = dict(nombre = 'susana', edad = 40, ciudad = 'matanzas')
print(diccionario)
# si quiero saber un un valor de mi diccionario llamo a la llave
valor = diccionario['edad']
print(valor)
diccionario['sexo']= 'femenino'

diccionario['correo']= 'dayi@fgh.com'
print(diccionario)

# tiene una serie de metodos que lo pueden ver como vimos anteriormente dir(diccionario)
#try except
try:
    print(diccionario['apellido'])
except:
    print('no se encuentra la llave ')
# aunque no lo crean ya hemos visto funciones en este codigo por ejemplo aqui casa.append('cerro') con el len 
# ya esas son llamandas a funciones que estan definidas para crear algo 
#Entonces una funcion son bloques de códigos para mostrar una serie de resultados mas complejos
#  y que quiero que lo haga repetidamente sin tener que escribir el código una y otra vez, y solo se ejecuta cuando 
# este es llamado 
#tenemos las llamadas de funciones internas de python como vimos mas arriba con len type dir son funciones que ya estan predefinidas en python
#Para finalizar la función, debes introducir una línea vacía (esto no es necesario en
#un script).
#Al definir una función se crea una variable con el mismo nombre.
def salario_trabajador():
    salario_x_hora = 8 
    jornada = float(input('introduzca la cantidad de horas que trabaja por dia: '))
    cantidad_de_dias_trabajados = float(input('cuantos dias trabajo en el mes: '))
    salario_que_recibe = cantidad_de_dias_trabajados *  (jornada * salario_x_hora)
    print(f'SU salario este mes sera: {salario_que_recibe} dolares')
    if salario_que_recibe >= 500:
        print(f'puede vivir con eso en un año tendra {salario_que_recibe * 12} ')
    else:
        print ('pida ayuida al gobierno' )

salario_trabajador()