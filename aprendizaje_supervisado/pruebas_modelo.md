
# Documento de pruebas del modelo de transporte

## 1. Objetivo

Verificar que el modelo de regresion lineal del proyecto Sistema Inteligente de Rutas cargue los datos, entrene correctamente y genere predicciones y una grafica.

## 2. Entorno de ejecucion

- Lenguaje: Python.
- Bibliotecas: pandas, matplotlib y scikit-learn.
- Archivo de datos: datos_transporte.csv.
- Archivo del modelo: modelo_transporte.py.

## 3. Pruebas realizadas

### Prueba 1. Carga de datos

- Accion: cargar el archivo CSV.
- Resultado esperado: leer los registros y mostrar las primeras filas.
- Resultado obtenido: se cargaron 29 registros correctamente.
- Estado: APROBADA.

### Prueba 2. Division de datos

- Accion: separar los datos de entrenamiento y prueba.
- Resultado esperado: utilizar el 80 % para entrenamiento y el 20 % para prueba.
- Resultado obtenido: 23 registros de entrenamiento y 6 de prueba.
- Estado: APROBADA.

### Prueba 3. Entrenamiento del modelo

- Accion: entrenar el modelo de regresion lineal.
- Resultado esperado: calcular los parametros del modelo.
- Resultado obtenido: pendiente aproximada de 3 e intercepto cercano a 0.
- Estado: APROBADA.

### Prueba 4. Predicciones

- Accion: comparar los tiempos esperados con los predichos.
- Resultado esperado: obtener valores cercanos a los datos de prueba.
- Resultado obtenido: las predicciones mostradas coincidieron con los tiempos esperados de los seis registros.
- Estado: APROBADA.

### Prueba 5. Grafica

- Accion: generar y guardar la grafica de prediccion.
- Resultado esperado: visualizar los datos simulados y la linea de regresion.
- Resultado obtenido: se genero la grafica y se guardo como grafica_prediccion.png.
- Estado: APROBADA.

## 4. Conclusiones

Las pruebas realizadas permiten comprobar que el programa carga los datos simulados, entrena el modelo de regresion lineal, genera predicciones y representa los resultados graficamente.

Los resultados son exactos debido a que el conjunto de datos fue construido con una relacion lineal de tres minutos por estacion. Por tanto, las pruebas verifican el funcionamiento del programa, pero no validan los tiempos reales del transporte publico.

## 5. Evidencias

- Archivo CSV con los datos simulados.
- Codigo fuente del modelo.
- Grafica de prediccion.
- Captura de la ejecucion en la terminal.
