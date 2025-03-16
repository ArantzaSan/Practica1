#Eliminación de elementos en listas con del()
hardware = ["Gael", "Arantza", "Diego"]
del hardware[0]
print (hardware)
#Eliminación de elementos en listas con remove()
colores = ['rojo', 'azul', 'verde', 'blanco']
colores.remove('azul')
print(colores)
#Eliminación con pop y almacenamiento
colores = ['rojo', 'azul', 'verde', 'blanco']
almacena_valor = colores.pop(2)
print('El color eliminado y almacenado es:', almacena_valor)
#Insertar elementos en listas Python con append()
colores = ['rojo', 'azul', 'verde', 'blanco']
colores.append('naranja')
print(colores)
#Insertar elementos en listas Python con insert()
colores = ['rojo', 'azul', 'verde', 'blanco']
colores.insert(0,'naranja')
print(colores)
