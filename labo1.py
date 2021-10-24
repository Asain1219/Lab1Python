#!/usr/bin/python3

test = False
rango = 0
while test == False:
    rango = input('Ingrese el iterador')
    try:
        rango = int(rango)
        test = True
    except:
        try:
            rango = float(rango)
            print('se eliminara el decimal de su entrada ya que es un float')
            test = True
        except:
            print('eso no es un int ni un float ponga un int o un float')

char = input('Ingrese el carácter')
if type(rango) == float:
    rango = int(rango)
cont = rango

print('Mi carne es B91476')

for i in range(rango):
    print(cont * '{}' .format(char))
    cont -= 1
