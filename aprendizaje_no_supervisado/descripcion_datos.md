
# Descripción de los datos
## Proyecto: Sistema Inteligente de Rutas
### Actividad: Aprendizaje no supervisado

## 1. Objetivo

El conjunto de datos se utiliza para aplicar un modelo de aprendizaje no supervisado mediante el algoritmo K-Means, con el propósito de identificar grupos de recorridos que tengan características similares.

## 2. Fuente de los datos

Los datos fueron construidos de forma simulada con fines académicos, debido a que para este ejercicio no se utilizó una fuente oficial de mediciones de recorridos del transporte público.

Por lo tanto, los valores no representan tiempos ni distancias reales de TransMilenio.

## 3. Descripción del conjunto de datos

El archivo utilizado se llama `datos_rutas_clustering.csv` y contiene 33 registros simulados. Cada registro representa un recorrido hipotético.

El conjunto de datos incluye las siguientes variables:

| Variable | Tipo de dato | Descripción |
|---|---|---|
| numero_estaciones | Numérico entero | Cantidad de estaciones del recorrido. |
| tiempo_minutos | Numérico entero | Tiempo estimado del recorrido en minutos. |
| distancia_km | Numérico decimal | Distancia estimada del recorrido en kilómetros. |

## 4. Preparación de los datos

Para aplicar el algoritmo se seleccionaron las tres variables numéricas. Posteriormente, se utilizó StandardScaler de scikit-learn para normalizarlas y facilitar el agrupamiento, evitando que las diferencias de escala influyeran excesivamente en el resultado.

## 5. Algoritmo utilizado

Se utilizó K-Means, un algoritmo de aprendizaje no supervisado que agrupa los registros de acuerdo con sus similitudes.

Para este ejercicio se configuraron tres grupos mediante el parámetro `n_clusters=3`. El modelo asignó automáticamente una etiqueta a cada recorrido.

## 6. Resultados esperados y obtenidos

El modelo identificó tres grupos de 11 recorridos cada uno:

- Grupo 0: recorridos largos, con un promedio de 30 estaciones, 77,73 minutos y 18,23 kilómetros.
- Grupo 1: recorridos cortos, con un promedio de 8 estaciones, 22,64 minutos y 5,05 kilómetros.
- Grupo 2: recorridos intermedios, con un promedio de 19 estaciones, 50,27 minutos y 11,48 kilómetros.

Estos resultados describen los patrones encontrados en los datos simulados y no deben interpretarse como mediciones reales del transporte público.

## 7. Archivos relacionados

- `datos_rutas_clustering.csv`: conjunto de datos de entrada.
- `modelo_rutas_clustering.py`: código fuente del modelo.
- `grafica_clustering.png`: representación gráfica de los grupos.
- `resultados_clustering.csv`: datos originales con la etiqueta asignada a cada registro.
