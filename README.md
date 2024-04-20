# Bayeta de la Fortuna

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