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
#método _init_
class Usuarios:
    def_init_(self, nombre, apellidos)
    self.nombre = nombre
    self.apellidos = apellidos

  def imprime_datos(self):
    print('Nombre:', self.nombre, '\nApellidos:', self.apellidos)

usuario001 = Usuario()
#self para clases
class Usuarios:
    def_init_(self, nombre, apellidos)
    self.nombre = nombre
    self.apellidos = apellidos

  def imprime_datos(self):
    print('Nombre:', self.nombre, '\nApellidos:', self.apellidos)

usuario001 = Usuario('Enrique', 'Barros Fernández')

usuario002 = Usuario('Javier', 'Gomila Reyes')

usuario002.nombre = 'Jacinto'

usuario002.imprime_datos()
#Declaración de clases vacías
# pass
class NombreClase
  pass
  #eliminar atributos de objetos
del nombre_objeto.atributo
  #eliminar objetos
del nombre_objeto
#Herencia de clases
  #esta es la superclase
class Usuarios:
    def_init_(self, nombre, apellidos)
    self.nombre = nombre
    self.apellidos = apellidos

  def imprime_datos(self):
    print('Nombre:', self.nombre, '\nApellidos:', self.apellidos)
    #esta es la subclase
  class UsuariosPremium(Usuarios):
    pass
  #como heredar init
#superclase
class Usuarios:
    def_init_(self, nombre, apellidos)
    self.nombre = nombre
    self.apellidos = apellidos

  def imprime_datos(self):
    print('Nombre:', self.nombre, '\nApellidos:', self.apellidos)
    #subclase
class UsuariosPremium(Usuarios):
  def_init_(self, nombre, apelllidos, instagram)
  self.nombre = nombre
  self.apellidos = apellidos
  self.instagram = instagram
  

    
    
