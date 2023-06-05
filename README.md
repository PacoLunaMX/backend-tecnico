# Test Técnico - FastAPI con MongoDB y Pytest

Ejercicio técnico para realizar un backend simple con Python, utilizando FastAPI como framework, MongoDB como base de datos no relacional, y pytest para correr las test de integración.

## Para correr el servidor:

Para poder iniciar el servidor es necesario agrega las siguientes variables de entorno en un archivo llamado `.env`. 

```
DB_NAME=<db_name>
COLLECTION_NAME=<collection_name>
CLUSTER_USERNAME=<cluster_name>
CLUSTER_PASSWORD=<cluster_password>
```

Instala las dependencias:

```
python pip install -r requirements.txt
```

Inicia el servidor:
```
python uvicorn app.main:app --reload
```

Cuando la aplicación inicie, navega a `http://localhost:8000/docs` y prueba los endpoints para  `usuarios`.

## Correr los tests

```
python pytest
```
