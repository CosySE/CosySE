
def procesar_archivo():

    nombre = input('Introduzca el nombre del archivo con su extension : \n')
    try:
        lectura = open(nombre)
    except:
        print('No se ha podido abrir el archivo especificado')
        exit()

    lectura = lectura.read()
    lectura = lectura.split()
    print(f'cantidad de palabras del text {len(lectura)}')
    return lectura

def cantidad_gerundios(cadena):
    can_gerundio = 0
    lista_gerundios =[]
    for palabra in cadena:
        if palabra.endswith('ando') or palabra.endswith('iendo'):
            can_gerundio = can_gerundio + 1
            lista_gerundios.append(palabra)
    print(f'la cantidad de gerundios es {can_gerundio} y son {lista_gerundios} ')            

def contar_palabras(cadena):
    diccionario = {}
    lista_palabras_repetidas=[]
    for palabra in cadena:
        diccionario[palabra]=diccionario.get(palabra,0) + 1
    
    for llave,valor in diccionario.items():
        if valor >= 10:
            lista_palabras_repetidas.append(llave)
    print(f'las palabras mas repetidas son: {lista_palabras_repetidas}') 
    #print(diccionario)

if __name__=='__main__':
    #procesar_archivo()
    contar_palabras(procesar_archivo())
    cantidad_gerundios(procesar_archivo())
