# Importa las bibliotecas necesarias
import matplotlib.pyplot as plt
from typing import List, Tuple
import random

def cosmic_function(data: List[float]) -> Tuple[float, float]:
    # Cálculo del promedio
    average = sum(data) / len(data)
    
    # Cálculo de la desviación estándar
    deviation = (sum((x - average) ** 2 for x in data) / len(data)) ** 0.5
    
    return average, deviation

# Genera algunos datos para la prueba
data = [random.gauss(0, 1) for _ in range(1000)]

# Calcula la media y la desviación estándar
average, deviation = cosmic_function(data)

# Crea un histograma de los datos
plt.hist(data, bins=30, alpha=0.5)

# Añade una línea para la media
plt.axvline(average, color='r', linestyle='dashed', linewidth=1)
plt.text(average*1.1, plt.ylim()[1]*0.9, 'Media: {:.2f}'.format(average))

# Añade líneas para la desviación estándar
plt.axvline(average - deviation, color='g', linestyle='dashed', linewidth=1)
plt.text((average - deviation)*0.9, plt.ylim()[1]*0.8, 'Desviación estándar: {:.2f}'.format(deviation))
plt.axvline(average + deviation, color='g', linestyle='dashed', linewidth=1)

# Muestra la gráfica
plt.show()
