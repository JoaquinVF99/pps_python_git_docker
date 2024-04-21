# Bayeta de la Fortuna

![logo](panda.png) 

¡Bienvenido a la Bayeta de la Fortuna! Esta aplicación te provee de frases auspiciosas para iluminar tu día y guiarte hacia el éxito.

## Descripción

Esta aplicación web utiliza Flask para proporcionar un servicio que genera frases auspiciosas de forma aleatoria. Puedes acceder a una única frase auspiciosa en la raíz del servidor (`/`) o especificar el número de frases que deseas obtener en la ruta `/frotar/<n_frases>`, donde `<n_frases>` es un número entero.

## Uso

1. Clona este repositorio en tu máquina local:

```
git clone https://github.com/JoaquinVF99/pps_python_git_docker
cd pps_python_git_docker
```

2. Instala las dependencias necesarias utilizando pip:

```
pip install -r requirements.txt
```

3. Ejecuta la aplicación Flask:

```
python app.py
```

4. Accede a la aplicación en tu navegador web:

- Para obtener una sola frase auspiciosa: [http://localhost:5000/](http://localhost:5000/)
- Para obtener múltiples frases auspiciosas: [http://localhost:5000/frotar/<n_frases>](http://localhost:5000/frotar/<n_frases>)

Recuerda reemplazar `<n_frases>` con el número de frases que deseas obtener.


## Construir con Docker

Si prefieres utilizar Docker, puedes seguir estos pasos:

1. Construye la imagen Docker:

```bash
docker build -t bayeta-de-la-fortuna .
```

2. Despliega un contenedor:
```
docker run -d -p 5000:5000 bayeta-de-la-fortuna

```
3. Prueba que funcione:  

Accede a http://localhost:5000/ en tu navegador para verificar que la aplicación Flask esté funcionando correctamente. También puedes utilizar herramientas como curl o wget para enviar solicitudes HTTP al servidor Flask y verificar las respuestas.

## Conexión a MongoDB

La aplicación utiliza una base de datos MongoDB para almacenar las frases auspiciosas. MongoDB es una base de datos NoSQL que ofrece flexibilidad y escalabilidad para manejar grandes volúmenes de datos de manera eficiente.

La conexión a MongoDB se establece utilizando la biblioteca pymongo en Python. La aplicación se conecta al servidor de MongoDB y accede a una base de datos llamada 'bayeta' y a una colección llamada 'frases_auspiciosas' para almacenar las frases auspiciosas.

La base de datos y la colección deben estar configuradas previamente en MongoDB antes de ejecutar la aplicación. Asegúrate de que MongoDB esté en ejecución y accesible desde la aplicación antes de iniciarla.

La función `frotar()` en el archivo `bayeta.py` es responsable de realizar la conexión a MongoDB, recuperar las frases auspiciosas de la colección y seleccionar frases aleatorias para mostrar en la aplicación.

Si deseas modificar la conexión a MongoDB o la estructura de la base de datos, puedes hacerlo editando el archivo `bayeta.py` y ajustando los parámetros de conexión y consulta según sea necesario.

## Despliegue con Docker Compose

Si prefieres utilizar Docker para desplegar la aplicación y la base de datos, puedes utilizar Docker Compose para simplificar el proceso de gestión de los contenedores.

1. Asegúrate de tener Docker y Docker Compose instalados en tu sistema.

2. Crea un archivo `docker-compose.yml` en la raíz del proyecto y copia el siguiente contenido:

```yaml
version: '3.8'

services:
  mongodb:
    image: mongo:latest
    container_name: <mongo<db-container>
    ports:
      - "27017:27017"
    volumes:
      - mongodb-data:/data/db

  flask-app:
    build: .
    container_name: <flask-app-container>
    ports:
      - "5000:5000"
    depends_on:
      - mongodb

volumes:
  mongodb-data:
    driver: local

```
3. Abre una terminal en la raíz del proyecto y ejecuta el siguiente comando para iniciar los contenedores en segundo plano:
```
docker-compose up -d
```

Esto creará y ejecutará los contenedores de la aplicación Flask y MongoDB en segundo plano.

4. Accede a la aplicación en tu navegador web:
* Para obtener una sola frase auspiciosa: http://localhost:5000/
* Para obtener múltiples frases auspiciosas: http://localhost:5000/frotar/<n_frases>
* Recuerda reemplazar <n_frases> con el número de frases que deseas obtener.

5. Cuando hayas terminado de utilizar la aplicación, puedes detener los contenedores utilizando el siguiente comando:

```
docker-compose down
```

Esto detendrá y eliminará los contenedores, pero mantendrá los datos persistentes del volumen mongodb-data.