## Gestión de Datos de Países en Python (ver en formato raw)



### Descripción del Proyecto



Este proyecto consiste en una aplicación desarrollada en Python para la gestión de información de países mediante una interfaz de consola.
La aplicación permite cargar, consultar, modificar y analizar datos almacenados en un archivo CSV. Para el procesamiento de la información se utilizan estructuras como listas, diccionarios y funciones, permitiendo una organización clara y eficiente de los datos.
Entre sus principales funcionalidades se encuentran la búsqueda de países, el filtrado por distintos criterios, el ordenamiento de registros y la generación de estadísticas sobre la información almacenada.



### Objetivos



* Aplicar estructuras de datos como listas, diccionarios y tuplas.
* Utilizar archivos CSV.
* Implementar programación modular mediante funciones.
* Realizar búsquedas y filtros de información.
* Generar estadísticas básicas.
* Aplicar validaciones y manejo de errores.



### Tecnologías Utilizadas

* Python
* CSV (Comma Separated Values)
* Git
* GitHub
* Visual Studio Code



### Estructura del Proyecto



TPI-Gestion-Paises-Python
│
├── main.py
├── paises.csv
├── README.md



### Dataset Utilizado



Cada país contiene los siguientes datos:



* Nombre
* Población
* Superficie
* Continente



Ejemplo:



Nombre,Población,Superficie,Continente


Argentina,45376763,2780400,América
Brasil,213993437,8515767,América
Japón,125800000,377975,Asia



### Funcionalidades Implementadas


###### Mostrar Países


Permite visualizar todos los países cargados en el sistema.



###### Agregar País



Permite agregar nuevos países verificando:



* Campos obligatorios.
* Datos numéricos válidos.
* Valores mayores que cero.
* Evitar registros duplicados.


###### Actualizar País



Permite modificar:



* Población.
* Superficie.



De un país existente.



###### Buscar País



Permite realizar búsquedas:



* Exactas.
* Parciales.



Por nombre.



###### Filtrar Países



Filtrado por:



* Continente.
* Rango de población.
* Rango de superficie.


###### Ordenar Países



Ordenamiento por:

* Nombre.
* Población.
* Superficie.



En forma ascendente o descendente.



###### Estadísticas



El sistema calcula:



* País con mayor población.
* País con menor población.
* Promedio de población.
* Promedio de superficie.
* Cantidad de países por continente.



###### Validaciones Implementadas



Se implementaron validaciones utilizando:



* try
* except
* raise ValueError



Para evitar:



* Campos vacíos.
* Ingreso de texto en campos numéricos.
* Ingreso de números en campos de texto.
* Valores negativos.
* Búsquedas inexistentes.
* Errores de lectura del CSV.



###### Ejemplo de Uso


Menú Principal

1. Mostrar países
2. Agregar país
3. Actualizar país
4. Buscar país
5. Filtrar por continente
6. Filtrar por población
7. Filtrar por superficie
8. Ordenar países
9. Mostrar estadísticas
10. Salir


###### Ejemplo de Búsqueda



Entrada: 



Argentina



Salida:



Nombre: Argentina
Población: 45376763
Superficie: 2780400
Continente: América



### Participación de los Integrantes



* Mayco Zapata
* Luis Sosa



###### Responsabilidades:



* Diseño del sistema.
* Implementación de funcionalidades.
* Desarrollo de validaciones.
* Implementación de filtros.
* Implementación de estadísticas.
* Elaboración de documentación.
* Pruebas y corrección de errores.

