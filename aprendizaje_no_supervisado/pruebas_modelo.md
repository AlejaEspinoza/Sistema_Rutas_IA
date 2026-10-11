
# Pruebas del modelo de aprendizaje no supervisado
## Proyecto: Sistema Inteligente de Rutas

## 1. Objetivo de las pruebas

Verificar el funcionamiento del programa desarrollado en Python para aplicar el algoritmo K-Means y agrupar recorridos según el número de estaciones, el tiempo estimado y la distancia.

## 2. Entorno de ejecución

- Lenguaje: Python.
- Bibliotecas: pandas, matplotlib y scikit-learn.
- Algoritmo: K-Means.
- Archivo de entrada: datos_rutas_clustering.csv.

## 3. Pruebas realizadas

### Prueba 1. Carga de los datos

**Procedimiento:** ejecutar el programa y comprobar la lectura del archivo CSV.

**Resultado esperado:** el programa muestra los primeros registros y la cantidad total de recorridos.

**Resultado obtenido:** satisfactorio. Se cargaron 33 registros simulados.

### Prueba 2. Preparación de las variables

**Procedimiento:** seleccionar las tres variables numéricas y aplicar StandardScaler.

**Resultado esperado:** las variables quedan preparadas y normalizadas para el agrupamiento.

**Resultado obtenido:** satisfactorio. El programa continuó con el entrenamiento sin errores.

### Prueba 3. Agrupamiento mediante K-Means

**Procedimiento:** ejecutar el modelo con tres grupos.

**Resultado esperado:** el algoritmo asigna una etiqueta a cada recorrido.

**Resultado obtenido:** satisfactorio. Se generaron tres grupos con 11 recorridos cada uno.

### Prueba 4. Cálculo de promedios

**Procedimiento:** calcular el promedio de estaciones, tiempo y distancia para cada grupo.

**Resultado esperado:** se muestran las características promedio de los grupos identificados.

**Resultado obtenido:** satisfactorio. Se obtuvieron los siguientes resultados:

| Grupo | Estaciones promedio | Tiempo promedio | Distancia promedio |
|---|---:|---:|---:|
| 0 | 30,00 | 77,73 min | 18,23 km |
| 1 | 8,00 | 22,64 min | 5,05 km |
| 2 | 19,00 | 50,27 min | 11,48 km |

### Prueba 5. Generación de la gráfica

**Procedimiento:** ejecutar la sección de visualización del programa.

**Resultado esperado:** se genera y guarda una gráfica que distingue los tres grupos.

**Resultado obtenido:** satisfactorio. Se generó el archivo grafica_clustering.png.

### Prueba 6. Guardado de resultados

**Procedimiento:** comprobar la creación del archivo de salida.

**Resultado esperado:** se guarda un CSV con los datos originales y la etiqueta de grupo asignada.

**Resultado obtenido:** satisfactorio. Se generó el archivo resultados_clustering.csv.

## 4. Conclusión

Las pruebas realizadas permitieron comprobar que el programa carga los datos, prepara las variables, aplica K-Means, calcula los promedios de los grupos y genera los archivos de resultados.

El ejercicio demuestra el funcionamiento del aprendizaje no supervisado con datos simulados. Para obtener conclusiones sobre el transporte público real, sería necesario utilizar datos reales de recorridos, tiempos y distancias.
