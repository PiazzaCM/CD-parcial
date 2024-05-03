import pandas as pd
import matplotlib.pyplot as plt

# Definimos una lista de diccionarios, donde cada diccionario representa un estudiante y sus calificaciones en diferentes asignaturas.
calificaciones = [
    {"nombre": "Juan", "matematicas": 85, "ciencias": 90, "historia": 75},
    {"nombre": "María", "matematicas": 70, "ciencias": 80, "historia": 85},
    {"nombre": "Pedro", "matematicas": 95, "ciencias": 75, "historia": 90},
    {"nombre": "Ana", "matematicas": 80, "ciencias": 85, "historia": 80},
    {"nombre": "Luis", "matematicas": 75, "ciencias": 70, "historia": 95},
    {"nombre": "Sofía", "matematicas": 90, "ciencias": 85, "historia": 75},
    {"nombre": "Carlos", "matematicas": 85, "ciencias": 90, "historia": 80},
    {"nombre": "Elena", "matematicas": 70, "ciencias": 75, "historia": 85},
    {"nombre": "Javier", "matematicas": 80, "ciencias": 85, "historia": 90},
    {"nombre": "Laura", "matematicas": 75, "ciencias": 70, "historia": 95},
    {"nombre": "Diego", "matematicas": 90, "ciencias": 85, "historia": 75},
    {"nombre": "Paula", "matematicas": 85, "ciencias": 90, "historia": 80},
    {"nombre": "Carmen", "matematicas": 70, "ciencias": 75, "historia": 85}
]
# Creamos un Data Frame a partir de la lista dada
data_frame = pd.DataFrame(calificaciones)

# Función para calcular el promedio de una materia
def calcular_promedio(data_frame, materia):
    # Creamos un Data Frame con las calificaciones de la materia que especifiquemos
    dataframe_promedio = pd.DataFrame(data_frame[f'{materia}'])
    # Calculamos la suma acumulativa de las calificaciones
    dataframe_promedio['Fi'] = dataframe_promedio[f'{materia}'].cumsum()
    # Calculamos el promedio el número de estudiantes.
    promedio = dataframe_promedio['Fi'][12] / 12 
    return f"El promedio para la materia: {materia} es: {promedio}"

#se imprime el promedio de las materias
print(calcular_promedio(data_frame, 'matematicas'))
print(calcular_promedio(data_frame, 'historia'))
print(calcular_promedio(data_frame, 'ciencias'))


# se define la funcion para encontrar la calificación más alta de una materia
def encontrar_calf_mas_altas(data_frame, materia):
    # Creamos un nuevo DataFrame con los nombres de los estudiantes y sus calificaciones en la materia especificada.
    order = pd.DataFrame(data_frame[['nombre', f'{materia}']])
    # Ordenamos el DataFrame en orden descendente de calificaciones.
    order.sort_values(by=f'{materia}', ascending=False, inplace=True)
    # Devolvemos el nombre del estudiante con la calificación más alta y la calificación.
    return f"La calificación más alta en {materia} es de {order.iloc[0]['nombre']}, con una calificación de {order.iloc[0][materia]}"
#se imprime la calificación más alta de una materia y el alumno que la tiene, este puede ser cambiado para otra asignatura dada anteriormente
print(encontrar_calf_mas_altas(data_frame, 'matematicas'))
print(encontrar_calf_mas_altas(data_frame, 'historia'))
print(encontrar_calf_mas_altas(data_frame, 'ciencias'))

# Función para calcular el porcentaje de estudiantes que aprobaron una materia específica.
def porcentaje_aprobados(data_frame, materia):
    # Creamos un nuevo DataFrame con los estudiantes que aprobaron la materia (calificación >= 60).
    aprobados = data_frame[data_frame[materia] >= 60]
    # Calculamos el porcentaje de estudiantes que aprobaron.
    porcentaje = (len(aprobados) / len(data_frame)) * 100
    return f'El porcentaje que aprobaron {materia} con mas del 60% es de es de {porcentaje}%'

#se imprime la calificación más alta de una materia y el alumno que la tiene, este puede ser cambiado para otra asignatura dada anteriormente
print(porcentaje_aprobados(data_frame, 'matematicas'))
print(porcentaje_aprobados(data_frame, 'historia'))
print(porcentaje_aprobados(data_frame, 'ciencias'))

# Calculamos el promedio de las notas de las asignaturas para cada estudiante
data_frame['Promedio'] = data_frame[['matematicas', 'ciencias', 'historia']].mean(axis=1)

# se crea un nuevo Data Frame con el nombre del estudiante y el promedio de cada uno
promedio_notas = data_frame[['nombre', 'Promedio']]

print(promedio_notas)


#punto 3

# Definimos los datos para el eje x e y
x = promedio_notas['nombre']
y = promedio_notas['Promedio']

# Creamos el gráfico de barras
plt.bar(x, y)

# Añadimos títulos y etiquetas
plt.title('Promedio de calificaciones por estudiante')
plt.xlabel('Estudiantes')
plt.ylabel('Promedio de calificaciones')

# Mostramos el gráfico
plt.show()


