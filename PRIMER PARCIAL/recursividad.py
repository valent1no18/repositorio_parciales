superheroes = [
    "Spider-Man",
    "Iron Man",
    "Capitán América",
    "Thor",
    "Hulk",
    "Black Widow",
    "Doctor Strange",
    "Wolverine",
    "Deadpool",
    "Storm",
    "Jean Grey",
    "Scarlet Witch",
    "Black Panther",
    "Ant-Man",
    "Daredevil"
]

# función recursiva   para buscar, determinar si Capitán América está en la lista.
def busqueda(array, value):
    tamañoarray = len(array) - 1
    if array[tamañoarray] == value:
        return f"El {value} se encuentra en la posición: {tamañoarray}"
    elif tamañoarray == 0:
        return f"El {value} no se encuentra en la lista"
    else:
        return busqueda(array[0:tamañoarray], value)

value = "Capitán América"
print(busqueda(superheroes, value))

# Función recursiva para listar los superhéroes de la lista:
def listar(array, index):
    if index < len(array):
        print(array[index])
        listar(array, index + 1)
 

listar(superheroes, 0)