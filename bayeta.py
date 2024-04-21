import random
from pymongo import MongoClient

def frotar(n_frases: int = 1) -> list:
    """
    Función para consultar frases auspiciosas aleatorias desde la base de datos MongoDB.
    """
    # Conexión con el motor de MongoDB
    client = MongoClient('mongodb', 27017)  # Nombre del contenedor de MongoDB

    # Obtener la base de datos y la colección
    db = client['bayeta']
    collection = db['frases_auspiciosas']
    
    # Obtener todas las frases de la colección
    todas_frases = [frase['frase'] for frase in collection.find()]

    # Seleccionar N frases únicas aleatorias de la lista de frases
    frases_seleccionadas = random.sample(todas_frases, min(n_frases, len(todas_frases)))

    return frases_seleccionadas

def insertar_frases(frases):
    """
    Función para insertar frases en la colección de MongoDB.
    """
    client = MongoClient('mongodb', 27017)  # Nombre del contenedor de MongoDB
    db = client['bayeta']
    collection = db['frases_auspiciosas']
    collection.insert_many(frases)

if __name__ == "__main__":
    # Ejemplo de uso de la función
    frases_aleatorias = frotar(3)
    for frase in frases_aleatorias:
        print(frase)

    frases_nuevas = [
        {"frase": "Nueva frase auspiciosa 1"},
        {"frase": "Nueva frase auspiciosa 2"}
    ]
    insertar_frases(frases_nuevas)