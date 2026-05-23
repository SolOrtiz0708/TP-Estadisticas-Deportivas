import csv

total_goles = 0
goles_por_jugador = {}

with open('estadisticas.csv', newline='') as archivo:
    lector = csv.DictReader(archivo)
    
    for fila in lector:
        jugador = fila['jugador']
        goles = int(fila['goles'])
        
        total_goles += goles
        
        if jugador in goles_por_jugador:
            goles_por_jugador[jugador] += goles
        else:
            goles_por_jugador[jugador] = goles

max_jugador = max(goles_por_jugador, key=goles_por_jugador.get)

print("Total de goles:", total_goles)
print("Jugador con más goles:", max_jugador)
-
