#Andres Mayorga
#Ejemplo Graficas
import numpy as np
import matplotlib.pyplot as plt
rng = np.random.default_rng(42)

# Datos de calificaciones de los estudiantes
matematicas = rng.integers(50, 100, 20)
ciencias = rng.integers(40, 95, 20)
literatura = rng.integers(60, 100, 20)

# Datos de errores para el gráfico de barras de error
errores_matematicas = rng.uniform(2, 5, 2)
errores_matematicas = [min(errores_matematicas), max(errores_matematicas)]

errores_ciencias = rng.uniform(1, 4, 2)
errores_ciencias = [min(errores_ciencias), max(errores_ciencias)]

errores_literatura = rng.uniform(3, 6, 2)
errores_literatura = [min(errores_literatura), max(errores_literatura)]

"""
#Grafico de dispersion:

plt.scatter(matematicas, ciencias, color='blue')
plt.title('Relación entre las calificaciones de Matematicas y Ciencias')
plt.xlabel('Calificaciones de Matematicas')
plt.ylabel('Calificaciones de ciencias')
plt.show()

#Grafico de barras de error:

materias = ['Matemáticas', 'Ciencias', 'Literatura']
calificaciones = [matematicas.mean(), ciencias.mean(), literatura.mean()]
errores = [errores_matematicas, errores_ciencias, errores_literatura]

transposed_data = [list(column) for column in zip(*errores)] #Transformacion de datos para trabajar con los errores asimetricos

errores1=np.array(transposed_data) #Se convierte a array

plt.errorbar(materias, calificaciones, yerr=errores1, fmt='o', capsize=5)
plt.title('Calificaciones Promedio con barras de error')
plt.xlabel('Materias')
plt.ylabel('Calificación Promedio')
plt.show()
"""

#Histograma

plt.hist(matematicas, bins=10)
plt.title('Distribucion de las calificaciones de matematicas')
plt.xlabel('Calificaciones de matematicas')
plt.ylabel('Frecuencia')
plt.show()

