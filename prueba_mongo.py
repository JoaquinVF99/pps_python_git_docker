from pymongo import MongoClient

def instanciar():
    """
    Función para instanciar la conexión con el contenedor de MongoDB.
    Retorna el cliente, la base de datos y la colección.
    """
    # Conexión con el contenedor de MongoDB
    client = MongoClient('mongodb', 27017)  # Nombre del contenedor de MongoDB
    
    # Obtener la base de datos y la colección
    db = client['bayeta']
    collection = db['frases_auspiciosas']
    
    return client, db, collection

def inicializar(collection, file_path):
    """
    Función para inicializar la colección con datos, leídos de un archivo de texto.
    """
    # Leer datos del archivo de texto
    with open(file_path, 'r') as file:
        data = file.readlines()
    
    # Insertar datos en la colección
    for line in data:
        document = {'frase': line.strip()}  # Suponiendo un formato simple de una sola clave 'frase'
        collection.insert_one(document)

def consulta(collection):
    """
    Función para realizar una consulta a la colección y mostrar los resultados.
    """
    # Realizar consulta a la colección
    documents = collection.find()
    
    # Mostrar resultados
    for doc in documents:
        print(doc)

# Ejemplo de uso
if __name__ == "__main__":
    # Instanciar la conexión y obtener la colección
    client, db, collection = instanciar()
    
    # Inicializar la colección con datos del archivo de texto
    file_path = 'frases.txt'  # Ruta al archivo de texto con las frases
    inicializar(collection, file_path)
    
    # Consultar la colección y mostrar los resultados
    consulta(collection)
