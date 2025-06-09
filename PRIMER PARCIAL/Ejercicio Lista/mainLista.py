


from list_ import List
from queue_ import Queue
from superherosData import superheroesMarvel, personajesMarvel, order_by_name, order_by_nameReal, order_by_año

listPersonajes = List()
queueVillanos = Queue()
listPersonajes.add_criterion('name', order_by_name)
listPersonajes.add_criterion('nameReal', order_by_nameReal)
listPersonajes.add_criterion('año', order_by_año)

for personaje in personajesMarvel:
    persona_je = superheroesMarvel(
        name = personaje[0],
        nameReal = personaje[1],
        biografia = personaje[2],
        año = personaje[3],
        esVillano = personaje[4]
    )
    listPersonajes.append(persona_je)



# Listado ordenado de manera ascendente por nombre de los personajes.
print("Listado ordenado por nombres de los personajes:")
listPersonajes.sort_by_criterion('name')
listPersonajes.show()


# Determinar en qué posición está The Thing  y Rocket Raccoon .
def posiciones(lista):

    index1 = lista.search('The Thing', 'name')
    if index1 is not None:
        print(f"The Thing se encuentra en la posición: {index1}")

    index2 = lista.search('Rocket Raccoon', 'name')
    if index2 is not None:
        print(f"Rocket Raccoon se encuentra en la posición: {index2}")

# Listar todos los villanos de la lista.
def villanos(lista):
    print("Lista de villanos:")
    for personaje in lista:
        if personaje.esVillano == True:
            print(f"{personaje}")


# Poner todos los villanos en una cola para determinar luego cuales aparecieron antes de 1980 .
def colaVillanos(lista, cola):
    for personaje in lista:
        if personaje.esVillano == True:
            villano = personaje
            cola.arrive(villano)

    tamañoCola = cola.size()

    print("Cola de villanos con aparición antes de 1980:")
    for _ in range(tamañoCola):
        personajeVillano = cola.on_front()

        if personajeVillano.año < 1980:
            print(f"{personajeVillano}")
        cola.move_to_end()

# Listar los superhéroes que comienzan con  Bl , G , My , y W .
def BL_G_My_W(lista):
    print("Superhéroes que comienzan con  Bl , G , My , y W:")
    for personaje in lista:
        if personaje.esVillano == False and personaje.name.startswith(('Bl', 'G', 'My', 'W')):
            print(personaje)

#Listado de personajes ordenados por nombre real de manera ascendente de los personajes.
print()
print("Listado ordenado por nombres reales de los personajes:")
listPersonajes.sort_by_criterion('nameReal')
listPersonajes.show()

# Listado de superhéroes ordenados por fecha de aparición .
print()
print("Listado ordenado por fecha de aparición:")
listPersonajes.sort_by_criterion('año')
listPersonajes.show()

# Modificar el nombre real de  Ant Man a  Scott Lang .
def modificarNombre(lista):
    index = lista.search('Ant Man', 'name')
    if index:
        print("Nombre anterior:")
        print(lista[index].nameReal)
        lista[index].nameReal = "Scott Lang"
        print("Nuevo nombre:")
        print(lista[index].nameReal)

# Mostrar los personajes que en su biografía incluyen la palabra viaje en el tiempo o traje .
def biografias(lista):
    print('Personajes que en su biografía incluyen la palabra viaje en el tiempo o traje')
    for personaje in lista:
        if 'viaje en el tiempo' in personaje.biografia or 'traje' in personaje.biografia:
            print(personaje)

# Eliminar a Electro y  Baron Zemo de la lista y mostrar su información si estaba en la lista.
def eliminarPersonajes(lista):
    index1 = lista.search('Electro', 'name')
    if index1 is not None:
        print(f"Personaje eliminado: {lista.delete_value('Electro', 'name')}")

    index2 = lista.search('Baron Zemo', 'name')
    if index2 is not None:
        print(f"Personaje eliminado:{lista.delete_value('Baron Zemo', 'name')}")



print()
posiciones(listPersonajes)
print()
villanos(listPersonajes)
print()
colaVillanos(listPersonajes, queueVillanos)
print()
BL_G_My_W(listPersonajes)
print()
print("Cambio de nombre de Ant Man:")
modificarNombre(listPersonajes)
print()
biografias(listPersonajes)
print()
eliminarPersonajes(listPersonajes)
