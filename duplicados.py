#se carga una lista de prueba
lista = [1,5, 8, 3, 2, 3, 4, 4, 8, 5, 6, 6, 7]

#se define la funcion 
def eliminar_duplicados(lista):
#validaciones de que la lista tenga datos 
    if not lista: 
        return 'no hay lista'
    elif len(lista) == 1: 
#se retorna la lista
        return lista
 #creamos una lista y se borran los duplicados
    nueva_lista = list(set(lista)) 
    return nueva_lista
#mostramos la lista
print(eliminar_duplicados(lista))
