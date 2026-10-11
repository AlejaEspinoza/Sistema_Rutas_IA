
# ============================================================
# PROYECTO: SISTEMA INTELIGENTE DE RUTAS
# ACTIVIDAD: APRENDIZAJE NO SUPERVISADO
# MODELO: K-MEANS
# ============================================================

# Importar pandas para leer y organizar los datos.
import pandas as pd

# Importar matplotlib para crear la grafica.
import matplotlib.pyplot as plt

# Importar KMeans para realizar el agrupamiento.
from sklearn.cluster import KMeans

# Importar StandardScaler para normalizar los datos.
from sklearn.preprocessing import StandardScaler

from pathlib import Path

# ------------------------------------------------------------
# 1. CARGAR EL CONJUNTO DE DATOS
# ------------------------------------------------------------

datos = pd.read_csv(
    Path(__file__).with_name("datos_rutas_clustering.csv")
)

print("DATOS DEL SISTEMA INTELIGENTE DE RUTAS")
print(datos.head())

print("\nCantidad total de recorridos:", len(datos))


# ------------------------------------------------------------
# 2. PREPARAR LOS DATOS
# ------------------------------------------------------------

# Seleccionar las variables que se utilizaran para agrupar.
X = datos[
    ["numero_estaciones", "tiempo_minutos", "distancia_km"]
]

# Normalizar las variables para que tengan una escala comparable.
escalador = StandardScaler()
X_escalado = escalador.fit_transform(X)

print("\nVariables utilizadas para el agrupamiento:")
print(X.columns.tolist())


# ------------------------------------------------------------
# 3. APLICAR EL ALGORITMO K-MEANS
# ------------------------------------------------------------

# Crear el modelo para identificar tres grupos.
modelo = KMeans(
    n_clusters=3,
    random_state=42,
    n_init=10
)

# Entrenar el modelo y asignar un grupo a cada recorrido.
datos["grupo"] = modelo.fit_predict(X_escalado)

print("\nRESULTADOS DEL AGRUPAMIENTO")
print(datos[["numero_estaciones", "tiempo_minutos",
             "distancia_km", "grupo"]])

print("\nCantidad de recorridos por grupo:")
print(datos["grupo"].value_counts().sort_index())


# ------------------------------------------------------------
# 4. MOSTRAR LAS CARACTERISTICAS DE LOS GRUPOS
# ------------------------------------------------------------

print("\nPROMEDIO DE CARACTERISTICAS POR GRUPO")
print(
    datos.groupby("grupo")[
        ["numero_estaciones", "tiempo_minutos", "distancia_km"]
    ].mean().round(2)
)


# ------------------------------------------------------------
# 5. GRAFICAR LOS GRUPOS ENCONTRADOS
# ------------------------------------------------------------

plt.figure(figsize=(10, 6))

for grupo in sorted(datos["grupo"].unique()):
    subconjunto = datos[datos["grupo"] == grupo]

    plt.scatter(
        subconjunto["numero_estaciones"],
        subconjunto["tiempo_minutos"],
        label=f"Grupo {grupo}"
    )

plt.title("Agrupamiento de recorridos mediante K-Means")
plt.xlabel("Numero de estaciones")
plt.ylabel("Tiempo estimado (minutos)")
plt.legend(title="Grupos identificados")
plt.grid(True)
plt.tight_layout()

# Guardar la grafica en la carpeta del proyecto.
plt.savefig(
    Path(__file__).with_name("grafica_clustering.png"),
    dpi=300
)

# Mostrar la grafica en pantalla.
plt.show()


# ------------------------------------------------------------
# 6. GUARDAR LOS RESULTADOS
# ------------------------------------------------------------

datos.to_csv(
    Path(__file__).with_name("resultados_clustering.csv"),
    index=False
)

print("\nSe guardaron los resultados en resultados_clustering.csv")
print("La grafica se guardo en grafica_clustering.png")
