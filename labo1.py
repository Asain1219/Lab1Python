#!/usr/bin/python3

test = False
rango = 0
while test == False:
    try:
        rango = float(input('Ingrese el iterador'))
        test = True
    except:
        print('eso no es un int ni un float ponga un int o un float')

if type(rango) == float:
        print ('se eliminara el decimal de su entrada ya que es un float')
        rango = int(rango)

char = input('Ingrese el carácter')
cont = rango

print('Mi carne es B91476')

for i in range(rango):
    print(cont * '{}' .format(char))
    cont -= 1
