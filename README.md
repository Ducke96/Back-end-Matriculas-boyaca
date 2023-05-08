# BACKEND PARA EL DESARROLLO DE UN DASHBOARD USANDO FLASK

Para el desarrollo de esta aplicacion se uso la informacion publica del SNIES perteneciente
al Ministerio de Educación Nacional.

## Requisitos para el proyecto

Para poder ejecutar correctamente el proyecto es necesario tener instalado `Python`,
ademas de un servidor de bases de datos como **[MySQL](https://dev.mysql.com/downloads/workbench/)** o `MariaDB`.

## Clonando del proyecto

Primero debe clonar este repositorio usando el comando:

```
$ git clone https://github.com/Ducke96/Back-end-Matriculas-boyaca.git
```

## Instalando el proyecto


Realice la instalación de las librerias necesarias para la ejecución del proyecto usando el comando

```
ENTRAR AL ENTORNO VIRTUAL GENERADO POR WILMAR HIGUERA 

CORRER : 

.\venv\Scripts\activate

Y EJECUTAR EL APP :

python -m flask  run --port 8000


```

Edite la configuración de usuario y contraseña de `MySQL` para la conexion de la base de datos en el archivo `/app.py`


La base de datos se encuenta en la carpeta MysqlDB , con el sql generador de la base de datos , junto con el csv de los datos filtrados


**NOTA:** debe crear previamente una base de datos para el proyecto y agregar el nombre a la configuración en el campo "[database_name]".

```
# Mysql Connection
app.config['MYSQL_HOST'] = 'localhost' 
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'database_name'


## Funcionamiento del proyecto

- Para ingresar a la API en el navegador ingrese el siguiente link <http://127.0.0.1:8000/api/>




1. Para hacer una peticion GET a cada una de las preguntas del dashboard:

```
GET http://localhost:8000/api/first_question/
GET http://localhost:8000/api/second_question/
GET http://localhost:8000/api/third_question/
GET http://localhost:8000/api/fourth_question/
GET http://localhost:8000/api/fifth_question/
GET http://localhost:8000/api/sixth_question/
GET http://localhost:8000/api/seventh_question/
```
