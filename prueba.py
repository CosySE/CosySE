# ##@version=5
# import math
# indicator("The Bear Bull Trap", overlay=true)

# ##Step 1

# candle_size1 =input(4.0, title='Step 1 candle Size % Daily')

# candle_size2 =input(0.5, title='Step 1 candle Size % Intraday')

# candle_size = timeframe.isdaily? candle_size1 : candle_size2

# big_red_candle = close<open and 100 - (close/open)*100>=candle_size

# big_green_candle = close>open and (close/open)*100 - 1OO>=candle_size

# #Retracement Range

# z = input(65,title='Inventory Retracement Percentage %', maxval=100)    

# hl = math.abs(high - low)

# Oc = math.abs(close - open)

# Max = math.max (cIose, open)

# min = math.min(close, open)

# top wick = high-max

# bot wick = min-low

# long_retraced = top_wick/hl >= z/100

# short_retraced =bot_wick/hl >= z/100

# ##// Step 3

# x1 = input(2.0, title='Step 3 Breakout % Daily')

# x2 = input(0.25, tit1e="Step 3 Breakout % Intraday")

# x = timeframe.isDaily? x1 : x2

# long2 = long_retraced and ta.barssince(big_red_candle )<=3

# short2 = short_retraced and ta.barssince(big_qreen_candIe)<=3

# longo = high>ta.vaIuewhen(Iong2 , max, O) * (1+x/100) and ta.barssince(Iong2 )<=3 and not Iong2

# shorto= low <ta.vaIuewhen(short2, min, 0) * (1-x/1OO) and ta.barssince(short2)<=3 and not short2

# long = Iong0 and not longo [1]

# short = short0 and not short0[1]

# ##// chart plot & alerts

# plotshape(long2, textcolor=color.lime, color=color.lime, style=shape.triangleup, text= , location=location.belowbar, offset=0, size=size.tiny)

# plotshape(short2, textcolor=color.red, color=color.red, style=shape.triangledown, text= , location=location.abovebar, offset=0, size=size.tiny)

# alertcondition(long2 , title='Step 2 BUY Alert')

# alertcondition(short2 , title='Step 2 SELL Alert')

# bgcolor(long?color.new(color.green, 70):short?color.new(color.red, 70):na)




# n = int(input().strip())
# if 1 <= n <= 100:
#     if 2<= n <=5 and n % 2 == 0:
#         print('Not Weird')
#     if 6<= n <= 20 and n % 2 ==0:
#         print ('Weird')
#     if n > 20 and n % 2 == 0:
#         print('Not Weird')
#     if n % 2 != 0:
#         print('Weird')
# else:
#     print('Out of constraits')
################################################################
# a = int(input())
# b = int(input())
# if 1 <= a <= 10**10 and 1 <= b <= 10**10:
#     print(f'''
#         {a+b}
#         {a-b}
#         {a*b} 
#                 ''')
#################################################################################
# n = int(input())
# a = []
# a = list(range(0,n))
# if 1 <= n <=20:
#     for i in a:
#         print(i**2)
#################################################################
# def is_leap(year):
#     leap = False
#     if year % 4 == 0:
#         if year % 100 == 0:
#             if year % 400 == 0:
#                 leap = True
#         else:
#             leap = True
#     else:
#         leap = False

#     return print(leap)

# year = int(input())
# is_leap(year)
################################################################
# n = int(input())
# def fact (n):
#     if 1 <= n <= 150:

#         for i in range(1,n+1):
            
#             print(i , end='')
        
        
            
# fact(n)
############################triangulo rectangulo
# import math

# ab = int(input())
# bc = int(input())
# if 0 <= ab <= 100 and 0 <= bc <= 100: 
#     hip = math.sqrt(ab**2 + bc**2)
#     b = ma = hip/2
#     angle = (ma**2 + bc**2 - b**2)/(2*ma*bc)
#     abc = math.acos(angle)
#     print(f'{round(math.degrees(abc))}\N{DEGREE SIGN}')
 ###############Tuplas tabla hash

# n = int(input())
# integer_list = map(int, input().split())
# l = [n]
# # l.append(integer_list)
# for i in integer_list:
#     l.append(i)
# t = tuple(l)
# print(t)
# print(hash(t))
####################################################
# ¡Aprendamos sobre la comprensión de listas! Se le dan tres números enteros x, y y z que representan las dimensiones de un paralelepípedo junto con un número entero n. Imprime una lista de todas las coordenadas posibles dadas por (i,j,k) en una cuadrícula 3D donde la suma de i+j+k no es igual a n . Aquí, 0<i<x,0<j<y,0<k<z. Utilice listas de comprensión en lugar de bucles múltiples, como ejercicio de aprendizaje.

    #2
    #2
    #2
    #2   
#[[0, 0, 0], [0, 0, 1], [0, 1, 0], [0, 1, 2], [0, 2, 1], [0, 2, 2], [1, 0, 0], [1, 0, 2], [1, 1, 1], [1, 1, 2], [1, 2, 0], [1, 2, 1], [1, 2, 2], [2, 0, 1], [2, 0, 2], [2, 1, 0], [2, 1, 1], [2, 1, 2], [2, 2, 0], [2, 2, 1], [2, 2, 2]]

x = int(input())
y = int(input())
z = int(input())
n = int(input())

# coordenadas = [(i, j, k) for i in range(1, x) for j in range(1, y) for k in range(1, z) if (i + j + k) != n]
coordenadas = [ i, j, k for i in range(1, x): for j in range(1, y) :for k in range(1, z) ]
for coordenada in coordenadas:
    print(coordenada)
# a= [(b.append(i) for i in range(x) ): (b.append(j) for j in range(y)):( b.append(k) for k in range(z))]
# print(b)
# for i,j,k in [range(x),range(y),range(z)]:
#     b.append([i,j,k])
    # for j in range(y):
    #     b.append(j)
    #     for k in range(z):
    #         b.append(k)

# for x in range(3):,
#     b.append([x*3])
            

print(coordenadas)