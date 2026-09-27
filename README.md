# Sistema Inteligente de Rutas

## Descripción

Sistema inteligente desarrollado en Python para encontrar rutas
entre estaciones del sistema de transporte masivo.

El sistema utiliza una base de conocimiento representada mediante
servicios y estaciones, reglas lógicas para validar conexiones y
el algoritmo de búsqueda heurística A* para encontrar recorridos.

El sistema permite:

- Consultar estaciones disponibles.
- Seleccionar una estación de origen y una de destino.
- Encontrar rutas directas.
- Encontrar rutas que requieren transbordos.
- Identificar los servicios utilizados.
- Mostrar el punto donde se realiza un transbordo.
- Calcular la cantidad de estaciones y desplazamientos.
- Estimar el tiempo del recorrido.
- Ejecutar pruebas automáticas del sistema.

## Objetivo

Desarrollar un sistema inteligente capaz de encontrar una ruta entre
dos estaciones del sistema de transporte masivo a partir de una base
de conocimiento.

El sistema debe analizar las conexiones disponibles y utilizar
búsqueda heurística para determinar un recorrido, teniendo en cuenta
los servicios disponibles y la posibilidad de realizar transbordos.

Como criterio de costo académico, cada desplazamiento entre estaciones
tiene un valor de 1 y el tiempo estimado se calcula utilizando un valor
aproximado de 3 minutos por desplazamiento.

Estos tiempos son únicamente estimaciones utilizadas para el desarrollo
académico y no representan tiempos reales de operación del sistema de
transporte.

## Base de conocimiento

La base de conocimiento del sistema se encuentra en el archivo
`conocimiento.py`.

En este archivo se almacenan los servicios de transporte y los
recorridos de las estaciones. Esta información representa el
conocimiento que utiliza el sistema para analizar las posibles rutas.

La base de conocimiento permite:

- Registrar los servicios disponibles.
- Definir el orden de las estaciones de cada servicio.
- Identificar qué servicios conectan dos estaciones.
- Validar si una estación existe.
- Obtener las estaciones disponibles.
- Calcular un tiempo estimado según la cantidad de desplazamientos.

Además, se utilizan reglas lógicas para determinar si una estación
puede conectarse con otra y si un servicio cubre un determinado tramo.

### Reglas principales

El sistema utiliza reglas como:

1. Una estación es válida si existe en la base de conocimiento.
2. Dos estaciones están conectadas cuando aparecen como estaciones
   consecutivas dentro de un recorrido.
3. Un servicio cubre un tramo cuando contiene las dos estaciones
   correspondientes.
4. Si el servicio cambia durante el recorrido, se identifica un
   transbordo.
5. La cantidad de desplazamientos corresponde a la cantidad de
   estaciones recorridas menos una.

## Algoritmo de búsqueda A*

El archivo `busqueda.py` contiene la implementación del algoritmo de
búsqueda A* utilizado por el sistema.

A* combina el costo acumulado del recorrido con una estimación del
costo restante para determinar qué estación explorar.

La función utilizada es:

f(n) = g(n) + h(n)

Donde:

- `g(n)` representa el costo acumulado desde la estación de origen.
- `h(n)` representa la estimación del costo restante hasta el destino.
- `f(n)` representa el costo total estimado.

En este proyecto, cada desplazamiento entre estaciones tiene un costo
de 1.

El algoritmo mantiene una lista de estaciones pendientes de explorar y
selecciona la estación con menor costo estimado.

### Funciones principales

`heuristica()`:

Calcula la estimación del costo restante entre la estación actual y el
destino.

`obtener_vecinos()`:

Obtiene las estaciones conectadas directamente con la estación actual
a partir de los recorridos registrados.

`obtener_servicios_tramo()`:

Determina qué servicios conectan directamente dos estaciones
consecutivas.

`buscar_ruta()`:

Ejecuta el algoritmo A* y devuelve el recorrido encontrado, los
servicios utilizados y la cantidad de transbordos.

## Estructura del proyecto

El proyecto está organizado en los siguientes archivos:

```text
Sistema_Rutas_IA/
│
├── conocimiento.py
├── busqueda.py
├── main.py
├── pruebas.py
└── README.md

## Instalación y ejecución

### Requisitos

Para ejecutar el sistema se necesita:

- Python 3.x
- Visual Studio Code o cualquier editor de código.
- Git, para descargar el proyecto desde GitHub.

### Descargar el proyecto

Clonar el repositorio utilizando:

```bash
git clone URL_DEL_REPOSITORIO

## Resultados de las pruebas

El sistema cuenta con un archivo `pruebas.py` que permite verificar el
funcionamiento de la búsqueda de rutas.

Se realizaron tres pruebas principales:

### Prueba 1: Ruta directa

Se verifica una ruta entre:

- Origen: Portal 20 de Julio
- Destino: Museo Nacional

El sistema encuentra una ruta directa utilizando el servicio `D81` y no
requiere transbordos.

**Resultado: APROBADA**

### Prueba 2: Ruta con transbordo

Se verifica una ruta entre:

- Origen: Portal Américas
- Destino: Toberín

El sistema encuentra una ruta utilizando los servicios `F51` y `G11`,
realizando un transbordo.

**Resultado: APROBADA**

### Prueba 3: Ruta entre portales

Se verifica una ruta entre:

- Origen: Portal 80
- Destino: Portal Norte - Unicervantes

El sistema encuentra una ruta directa utilizando el servicio `B10`.

**Resultado: APROBADA**

Las tres pruebas fueron ejecutadas mediante el comando:

```bash
python pruebas.py
```

El resultado de la ejecución confirmó que las pruebas fueron aprobadas.

## Ejemplos de ejecución

A continuación se presentan algunos ejemplos de ejecución del sistema.

### Ejemplo 1: Ruta directa

Origen:

`Portal 20 de Julio`

Destino:

`Museo Nacional`

Resultado:

- Servicio utilizado: D81
- Estaciones: 6
- Desplazamientos: 5
- Transbordos: 0
- Tiempo estimado: 15 minutos

### Ejemplo 2: Ruta con transbordo

Origen:

`Portal Américas`

Destino:

`Toberín`

Resultado:

- Servicios utilizados: F51 y G11
- Estaciones: 19
- Desplazamientos: 18
- Transbordos: 1
- Tiempo estimado: 54 minutos

El sistema identifica el transbordo durante el recorrido y muestra los
servicios utilizados.

### Ejemplo 3: Ruta entre portales

Origen:

`Portal 80`

Destino:

`Portal Norte - Unicervantes`

Resultado:

- Servicio utilizado: B10
- Estaciones: 15
- Desplazamientos: 14
- Transbordos: 0
- Tiempo estimado: 42 minutos

## Tecnologías utilizadas

El proyecto fue desarrollado utilizando las siguientes tecnologías:

- **Python:** lenguaje utilizado para desarrollar el sistema.
- **Visual Studio Code:** entorno utilizado para escribir y ejecutar el código.
- **Git:** herramienta utilizada para el control de versiones.
- **GitHub:** plataforma utilizada para almacenar y compartir el código fuente.
- **Algoritmo A*:** método de búsqueda heurística utilizado para encontrar
  recorridos.
- **Base de conocimiento:** estructura utilizada para representar los
  servicios y estaciones del sistema de transporte.

  ## Integrantes

- Maria Alejandra Espinoza Serrato

## Enlaces del proyecto

### Repositorio GitHub

https://github.com/AlejaEspinoza/Sistema_Rutas_IA.git

### Video de presentación

https://youtu.be/N4nwCWcYduY