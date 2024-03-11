# Datos de ejemplo: Se utilizan tres ciudades: Lago Agrio, Puyo y Quito.
# Cada ciudad tiene datos de temperatura para 4 semanas.
temperaturas = [
    {"ciudad": "Lago Agrio", "semana1": [30, 31, 32, 30, 31, 32, 33], "semana2": [31, 32, 33, 30, 31, 32, 33], "semana3": [32, 33, 34, 31, 32, 33, 34], "semana4": [33, 34, 35, 32, 33, 34, 35]},
    {"ciudad": "Puyo", "semana1": [18, 19, 18, 18, 19, 19, 20], "semana2": [19, 20, 21, 19, 20, 20, 21], "semana3": [20, 21, 22, 20, 21, 21, 22], "semana4": [21, 22, 23, 21, 22, 22, 23]},
    {"ciudad": "Quito", "semana1": [10, 12, 11, 10, 9, 8, 8], "semana2": [10, 11, 10, 9, 8, 8, 8], "semana3": [9, 10, 12, 11, 10, 8, 8], "semana4": [11, 12, 10, 9, 8, 8, 7]}
]

def calcular_temperatura_promedio(datos_temperatura): # Esta función toma una lista de diccionarios llamada datos_temperatura.
    """
    Calcula la temperatura promedio para cada ciudad.  # Para cada ciudad en los datos, calcula la temperatura promedio.

    Args:
        datos_temperatura (list): Lista de diccionarios con datos de temperatura.

    Returns:
        dict: Diccionario con las temperaturas promedio para cada ciudad.
    """
    temperaturas_promedio = {}
    for ciudad_data in datos_temperatura:
        ciudad = ciudad_data["ciudad"]
        temperaturas_semanales = []  # Combina las temperaturas de las cuatro semanas para obtener un promedio semanal.
        for semana in ["semana1", "semana2", "semana3", "semana4"]: # Luego, calcula el promedio general de todas las semanas.
            temperaturas_semanales.extend(ciudad_data[semana])
        temperatura_promedio = sum(temperaturas_semanales) / len(temperaturas_semanales)
        temperaturas_promedio[ciudad] = temperatura_promedio
    return temperaturas_promedio

# Ejemplo de uso
resultados = calcular_temperatura_promedio(temperaturas)
for ciudad, temperatura_promedio in resultados.items():
    print(f"Temperatura promedio en {ciudad}: {temperatura_promedio:.2f} °C")