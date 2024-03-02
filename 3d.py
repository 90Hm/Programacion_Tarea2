# Crear una matriz 3D para almacenar datos de temperaturas
# Primera dimensión: Ciudades (3 ciudades del Ecuador con climas diferentes)
# Segunda dimensión: Días de la semana (7 días)
# Tercera dimensión: Semanas (4 semanas)
temperaturas = [
    [   # Quito (frío y húmedo)
        [10, 12, 11, 10, 9, 8, 8],   # Semana 1
        [10, 11, 10, 9, 8, 8, 8],    # Semana 2
        [9, 10, 12, 11, 10, 8, 8],   # Semana 3
        [11, 12, 10, 9, 8, 8, 7]     # Semana 4
    ],
    [   # Lago Agrio (caliente y húmedo)
        [30, 31, 32, 30, 31, 32, 33],   # Semana 1
        [31, 32, 33, 30, 31, 32, 33],   # Semana 2
        [32, 33, 34, 31, 32, 33, 34],   # Semana 3
        [33, 34, 35, 32, 33, 34, 35]    # Semana 4
    ],
    [   # Baños (húmedo y templado)
        [18, 19, 18, 18, 19, 19, 20],   # Semana 1
        [19, 20, 21, 19, 20, 20, 21],   # Semana 2
        [20, 21, 22, 20, 21, 21, 22],   # Semana 3
        [21, 22, 23, 21, 22, 22, 23]    # Semana 4
    ]
]

# Nombres de las ciudades
ciudades = ["Quito", "Lago Agrio", "Baños"]

# Calcular el promedio de temperaturas para cada ciudad y semana
for ciudad_idx, ciudad in enumerate(temperaturas):
    for semana_idx, semana in enumerate(ciudad):
        total_temp = sum(semana)
        promedio_temp = total_temp / len(semana)
        print(f"Promedio de temperaturas para {ciudades[ciudad_idx]}, semana {semana_idx + 1}: {promedio_temp:.2f} °C")
