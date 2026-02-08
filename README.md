# Proyecto FastAPI

Esta version de la aplicacion corre enteramente en docker, por lo que lo unico que hay que hacer es crear los contenedores y crear la base de datos.

Para crear e iniciar los contenedores de docker ejecute el siguiente comando:
 - docker compose up -d
---
Una vez los contenedores de docker esten creados y corriendo, a traves de la pagina web de pgadmin4 hosteada en localhost:80 debera autenticarse con las credenciales especificadas en el archivo docker-compose.yaml

Las credenciales por defecto son las siguientes:
 - pgadmin4@pgadmin.org
 - admin

---

Una vez dentro de la pagina deberá añadir el servidor de la base de datos de odoo, creando una conexion con los siguientes parametros por defecto especificados en docker-compose.yaml:
 - Hostname: __db_fastapi__ | Nombre del contenedor de postgresql
 - Nombre de usuario: __odoo__ | Definido en el apartado environment
 - Contraseña: __odoo__ | Definido en el apartado environment

Una vez tenga creado el servidor debera crear la base de datos "fastapi-database"

---

Si ha seguido todos estos pasos, podra iniciar la API utilizando una de estas 2 opciones:

1. Ejecutando el archivo main.py con python # python .\main.py
2. Ejecutando el comando "uvicorn main:app"