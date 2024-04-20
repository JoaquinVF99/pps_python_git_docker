import random

def frotar(n_frases: int = 1) -> list:

    # Ruta al archivo de texto que contiene las frases auspiciosas
    archivo_frases = "frases.txt"

    # Lista para almacenar las frases auspiciosas
    frases_auspiciosas = []

    # Leer las frases del archivo de texto
    with open(archivo_frases, "r", encoding="utf-8") as file:
        for linea in file:
            # Eliminar los espacios en blanco al principio y al final de la línea
            linea = linea.strip()
            # Agregar la línea a la lista de frases auspiciosas
            frases_auspiciosas.append(linea)

    # Seleccionar N frases únicas aleatorias de la lista de frases
    frases_seleccionadas = random.sample(frases_auspiciosas, min(n_frases, len(frases_auspiciosas)))

    return frases_seleccionadas

