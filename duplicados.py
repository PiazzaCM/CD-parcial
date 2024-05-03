#se carga una lista de prueba
lista = [1,5, 8, 3, 2, 3, 4, 4, 8, 5, 6, 6, 7]

#se define la funcion con el parametro de entrada lista
def eliminar_duplicados(lista):
    #se retorna la lista eliminando los repetidos
    return list(set(lista))

#se imprime la lista sin los repetidos
print(eliminar_duplicados(lista))