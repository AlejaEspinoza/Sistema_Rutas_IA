
# ============================================================
# PROYECTO: SISTEMA INTELIGENTE DE RUTAS
# ACTIVIDAD 3: APRENDIZAJE SUPERVISADO
# MODELO: REGRESION LINEAL
# ============================================================

# Importar pandas para leer y organizar los datos.
import pandas as pd

# Importar matplotlib para crear la grafica de prediccion.
import matplotlib.pyplot as plt

# Importar LinearRegression para construir el modelo.
from sklearn.linear_model import LinearRegression

# Importar train_test_split para separar datos de entrenamiento y prueba.
from sklearn.model_selection import train_test_split

# ------------------------------------------------------------
# 1. CARGAR EL CONJUNTO DE DATOS
# ------------------------------------------------------------

# Leer el archivo CSV que contiene los datos simulados de transporte.
from pathlib import Path

datos = pd.read_csv(Path(__file__).with_name("datos_transporte.csv"))
# Mostrar los primeros registros para verificar que se cargaron.
print("DATOS DEL SISTEMA DE TRANSPORTE")
print(datos.head())

# Mostrar la cantidad de registros disponibles.
print("\nCantidad total de registros:", len(datos))


# ------------------------------------------------------------
# 2. PREPARAR LOS DATOS PARA EL APRENDIZAJE SUPERVISADO
# ------------------------------------------------------------

# X contiene la variable de entrada: numero de estaciones.
X = datos[["numero_estaciones"]]

# y contiene la etiqueta objetivo que queremos predecir:
# el tiempo estimado del recorrido en minutos.
y = datos["tiempo_minutos"]

# Dividir los datos en entrenamiento y prueba.
# El 20 % se reserva para evaluar el modelo.
X_entrenamiento, X_prueba, y_entrenamiento, y_prueba = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Mostrar la cantidad de datos de entrenamiento y prueba.
print("\nDATOS PARA EL ENTRENAMIENTO")
print("Registros de entrenamiento:", len(X_entrenamiento))
print("Registros de prueba:", len(X_prueba))


# ------------------------------------------------------------
# 3. ENTRENAR EL MODELO DE APRENDIZAJE SUPERVISADO
# ------------------------------------------------------------

# Crear el modelo de regresion lineal.
modelo = LinearRegression()

# Entrenar el modelo con los datos de entrenamiento.
modelo.fit(X_entrenamiento, y_entrenamiento)

# Generar predicciones para los datos de prueba.
predicciones = modelo.predict(X_prueba)

# Mostrar los resultados del entrenamiento.
print("\nRESULTADOS DEL MODELO")
print("Pendiente del modelo:", modelo.coef_[0])
print("Intercepto del modelo:", modelo.intercept_)

# Comparar los tiempos reales con los tiempos predichos.
print("\nCOMPARACION DE RESULTADOS")
for real, predicho in zip(y_prueba, predicciones):
    print(
        f"Tiempo esperado: {real:.2f} minutos | "
        f"Tiempo predicho: {predicho:.2f} minutos"
    )


# ------------------------------------------------------------
# 4. GRAFICAR LOS DATOS Y LAS PREDICCIONES
# ------------------------------------------------------------

# Crear valores ordenados para dibujar la linea de regresion.
X_grafica = pd.DataFrame({
    "numero_estaciones": sorted(X["numero_estaciones"])
})

# Calcular el tiempo estimado para cada valor de la grafica.
tiempos_grafica = modelo.predict(X_grafica)

# Crear la figura de la grafica.
plt.figure(figsize=(10, 6))

# Mostrar los datos originales como puntos azules.
plt.scatter(
    X["numero_estaciones"],
    y,
    color="blue",
    label="Datos simulados"
)

# Dibujar la linea de regresion aprendida por el modelo.
plt.plot(
    X_grafica["numero_estaciones"],
    tiempos_grafica,
    color="purple",
    label="Prediccion del modelo"
)

# Agregar titulo, nombres de los ejes y leyenda.
plt.title("Prediccion del tiempo segun el numero de estaciones")
plt.xlabel("Numero de estaciones")
plt.ylabel("Tiempo estimado (minutos)")
plt.legend()
plt.grid(True)

plt.tight_layout()

# Guardar la grafica como evidencia del modelo.
plt.savefig(Path(__file__).with_name("grafica_prediccion.png"), dpi=300)

# Mostrar la grafica en pantalla.
plt.show()
