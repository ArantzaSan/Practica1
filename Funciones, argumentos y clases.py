#Crear funciones
def saluda():
print("Bienvenidos")
saluda()
# *args en las funciones 
def alumnos(*args):
print('El primer alumno es ' + ' y el último es ' + args[3] + '.')
alumnos('Ana', 'Andrea', 'Antonio', 'Andrés')
# **kwargs
def colores (**kwargs):
print("Este es el color " + kwargs['color1'] + '.')
colores(color1='rojo', color2='azul')
#crear clases
class Usuario:
nombre = ''
apellidos = ''
def imprime datos(self)
print('Nombre:', self.nombre, '\nApellidos:', self.apellidos)

usuario001 = Usuario()

usuario001.nombre = 'Enrique'
usuario001.apellidos = 'Barros Fernández'
usuario001.imprime_datos()

