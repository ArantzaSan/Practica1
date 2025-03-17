#variables globles y locales
  def funcion1()
    global num1
    num1 = 10
funcion1()
print(num1)

#funciones anidadas
def funcion1():
  pass
def funcion2():
  print('String en la función anidada')

funcion1()
#import y lambda
import math

area = lambda radio: (math.pi * radio * radio)

print(area(2))
#mostrar fecha actual
import datetime
fecha = datetime.datetime.now()
print(fecha)

#fechas personalizadas
import datetime
fecha = datetime.datetime(2020, 9, 29, 19, 45)
print(fecha)
#expresiones regulares
import re
texto = "Bienvenidos a programación fácil"
busqueda = re.search("Bienvenidos", texto)
print(busqueda)

#función findall
import re
texto = "tres tristes tigres comen trigo en un trigal"
busqueda = re.findall("e", texto)
print(busqueda)

#función split()
import re
texto = "tres tristes tigres comen trigo en un trigal"
busqueda = re.split(" ", texto)
print(busqueda)

#método sub
import re
texto = "tres tristes tigres comen trigo en un trigal"
busqueda = re.sub(" ","-", texto)
print(busqueda)
