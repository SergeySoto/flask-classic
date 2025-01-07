# Aplicación de Flask con SQLite

Programa hecho en python con el framework, Hello world

## Instalación
- Crear un entorno en python y ejecutar el comando
```
pip install -r requirements.txt
```
La libreria utilizada en flask 
```
https://flask.palletsprojects.com/en/3.0.x/
```

## Ejecucion del programa

- iniciar el servidor de flask:
```set FLASK_APP=main.py```

## Otra opcion de ejecución
-Crear un archivo .env y dentro agregar lo siguiente:
```FLASK_APP=main.py```
```FLASK_DEBUG=True```
-y luego poder ejecutar en la terminal el comando:
```flask run```

## Comando para ejecutar el servidor
```flask --app main run```

## Comando para ejecutar el servidor en otro puerto diferente por default siempre es el 5000
```flask --app main run -p 5002```

## Comando para ejecutar el servidor en modo debug, para realizar cambios en tiempo real
```flask --app main --debug run```