from conocimiento import obtener_servicios
from busqueda import buscar_ruta


# PRUEBA 1: Ruta directa
origen = "Portal 20 de Julio"
destino = "Museo Nacional"

ruta = buscar_ruta(origen, destino)

assert ruta is not None, "ERROR: No se encontró la ruta."

assert ruta["transbordos"] == 0, (
    "ERROR: La ruta directa tiene transbordos."
)

assert "D81" in ruta["servicios"], (
    "ERROR: No se encontró el servicio D81."
)

print("PRUEBA 1: Ruta directa")
print("Resultado: APROBADA")
print("Ruta:", ruta["ruta"])
print("Servicios:", ruta["servicios"])
print("Transbordos:", ruta["transbordos"])

# PRUEBA 2: Ruta con transbordo
origen = "Portal Américas"
destino = "Toberín"

ruta = buscar_ruta(origen, destino)

assert ruta is not None, (
    "ERROR: No se encontró la ruta con transbordo."
)


assert ruta["transbordos"] >= 1, (
    "ERROR: No se encontró ningún transbordo."
)


assert "F51" in ruta["servicios"], (
    "ERROR: No se encontró el servicio F51."
)

assert "G11" in ruta["servicios"], (
    "ERROR: No se encontró el servicio G11."
)

print("\nPRUEBA 2: Ruta con transbordo")
print("Resultado: APROBADA")
print("Ruta:", ruta["ruta"])
print("Servicios:", ruta["servicios"])
print("Transbordos:", ruta["transbordos"])

# PRUEBA 3: Ruta directa entre portales
origen = "Portal 80"
destino = "Portal Norte - Unicervantes"

ruta = buscar_ruta(origen, destino)

assert ruta is not None, (
    "ERROR: No se encontró la ruta entre portales."
)

assert ruta["transbordos"] == 0, (
    "ERROR: La ruta entre portales tiene transbordos."
)

assert "B10" in ruta["servicios"], (
    "ERROR: No se encontró el servicio B10."
)

print("\nPRUEBA 3: Ruta entre portales")
print("Resultado: APROBADA")
print("Ruta:", ruta["ruta"])
print("Servicios:", ruta["servicios"])
print("Transbordos:", ruta["transbordos"])