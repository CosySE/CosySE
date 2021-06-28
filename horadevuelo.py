#Sabiendo la hora de salida de un vuelo en formato HH:mm:ss y el tiempo que demora en el mismo formato,
# se desea conocer el tiempo de llegada de dicho vuelo con una funcion que lo devuelva en string con el mismo formato HH:mm:ss

def ceroAlante(entero):
    if entero >= 0 and entero < 10:
        valor = str(0)+ str(entero)
    else:
        valor = str(entero)
    return valor

def tiempoLLegada(h_salida,t_vuelo):

    t_vuelo = t_vuelo.split(':')
    h_salida = h_salida.split(':')

    hora_salida =[]
    hora_vuelo = []

    for h in h_salida:
        hora_salida.append(int(h))
    #print(hora_salida)
    for v in t_vuelo:
        hora_vuelo.append(int(v))
    #print(hora_vuelo)
    seg_llegada = hora_salida[2] + hora_vuelo[2]
    min_llegada = hora_salida[1]+hora_vuelo[1]
    h_llegada = hora_salida[0]+hora_vuelo[0]
    if seg_llegada >= 60:
        seg_llegada = seg_llegada - 60
        min_llegada = min_llegada + 1
        #print(h_llegada,min_llegada,seg_llegada)
    if min_llegada >= 60:
        min_llegada = min_llegada - 60 
        h_llegada = h_llegada + 1
        #print(h_llegada,min_llegada,seg_llegada)
    if h_llegada >= 24:
        h_llegada = h_llegada - 24 
        #print(h_llegada,min_llegada,seg_llegada)
    return 'su vuelo llegara a las:'+ceroAlante(h_llegada)+':'+ceroAlante(min_llegada)+':'+ceroAlante(seg_llegada)


if __name__=='__main__':
    h_salida= input('hora salida: ')
    t_vuelo = input('tiempo que demora el vuelo: ')
    print(tiempoLLegada(h_salida,t_vuelo))
