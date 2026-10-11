
# Descripcion de los datos del proyecto

## 1. Nombre del proyecto

Sistema Inteligente de Rutas.

## 2. Fuente de los datos

Para esta actividad se construyo un conjunto de datos simulado con fines academicos, debido a que no se cuenta con una base de datos real de tiempos de desplazamiento del transporte publico.

Los datos representan una relacion hipotetica entre el numero de estaciones recorridas y el tiempo estimado del trayecto. Se asumio un tiempo de tres minutos por estacion.

Estos datos no corresponden a mediciones oficiales ni a tiempos reales del sistema de transporte.

## 3. Archivo utilizado

Nombre: datos_transporte.csv

El archivo contiene 29 registros y dos columnas.

## 4. Descripcion de las variables

- numero_estaciones: cantidad de estaciones del recorrido. Es la variable de entrada del modelo.
- tiempo_minutos: tiempo estimado del recorrido en minutos. Es la variable objetivo que el modelo busca predecir.

## 5. Uso de los datos

Los datos se utilizan para entrenar y evaluar un modelo de regresion lineal mediante la biblioteca scikit-learn de Python.

El conjunto se divide en datos de entrenamiento y datos de prueba. El 80 % se destina al entrenamiento y el 20 % a la prueba.

## 6. Limitaciones

Los datos son simulados y siguen una relacion lineal exacta de tres minutos por estacion. Por esta razon, los resultados sirven para demostrar el funcionamiento del algoritmo, pero no permiten afirmar que los tiempos reales del transporte publico sean iguales.

Para mejorar el modelo en el futuro, se podrian incorporar datos reales de rutas, distancias, transbordos, horarios y condiciones del trafico.
