#Se tiene una X en la esquina superior izquierda de un área de 4x4. Se tiene una matriz con 10 elementos. Cada 2 elementos de la matriz corresponden un movimiento, el primero en el eje horizontal y el Segundo en el eje vertical. El número indica las unidades a moverse y el signo la dirección (positive para derecho o abajo, negative para la izquierda o arriba)
#Por ejemplo para este juego de datos (1,2,-1,1,0,1,2,-1,-1,-2)
#La X se moverá una unidad a la derecho y dos hacia abajo y 
# así sucesivamente. El programa debe imprimir la posición final de la X y donde no la letra O,
#  si por la instrucción se le obliga a la X salir del lugar debe permanecer en el borde
# OXOO
# OOOO
# OOOO
# OOOO 

datos = (1,2,-1,1,0,1,2,-1,-1,2)
def principal(largo,ancho):
    f,c = 0,0
    for x in range(0,len(datos),2):
        vx = datos[x]
        vy = datos[x+1]
        print(vx,vy)
        matriz =[[k]*largo for k in ['O']*ancho]
        tam = len(matriz)
        print(posicion(vx,vy,tam,f,c))
        f,c = posicion(vx,vy,tam,f,c)
        matriz[f][c]='X'
        recorrer_matriz(matriz)
def posicion(vx,vy,tam,f=0,c=0):
    f = f + vy
    c = c + vx 
    if f >= tam-1:
        f = tam-1
    elif f <= 0:
        f = 0
    if c >= tam-1:
        c = tam-1
    elif c <= 0:
        c = 0
    return f,c
def recorrer_matriz(mtz):
    for m in mtz:
        print(m)

if __name__=='__main__':
    print(datos)
    principal(4,4)