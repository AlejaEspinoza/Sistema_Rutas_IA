# ==========================================
# SISTEMA INTELIGENTE DE RUTAS
# ==========================================

import unicodedata

from conocimiento import (
    servicios,
    estaciones_disponibles,
    estacion_valida,
    obtener_servicios,
    obtener_recorrido,
    calcular_tiempo_estimado
)

from busqueda import buscar_ruta
from busqueda import obtener_servicios_tramo


# ==========================================
# MOSTRAR ESTACIONES
# ==========================================

def mostrar_estaciones():
    print("\nESTACIONES DISPONIBLES")
    print("-" * 40)

    for estacion in estaciones_disponibles():
        print(f"- {estacion}")


# ==========================================
# BUSCAR NOMBRE DE ESTACIÓN
# ==========================================

def normalizar_texto(texto):
    """
    Convierte el texto a minúsculas y elimina las tildes.
    """

    texto = texto.strip().lower()

    texto = unicodedata.normalize(
        "NFD",
        texto
    )

    texto = "".join(
        caracter
        for caracter in texto
        if unicodedata.category(caracter) != "Mn"
    )

    return texto


def buscar_nombre_estacion(nombre):
    """
    Busca una estación ignorando:
    - Mayúsculas
    - Minúsculas
    - Tildes
    - Espacios innecesarios
    """

    nombre_normalizado = normalizar_texto(nombre)

    for estacion in estaciones_disponibles():

        estacion_normalizada = normalizar_texto(
            estacion
        )

        if estacion_normalizada == nombre_normalizado:
            return estacion

    return None


# ==========================================
# MOSTRAR SERVICIOS DIRECTOS
# ==========================================

def mostrar_servicios(origen, destino):

    servicios_disponibles = obtener_servicios(
        origen,
        destino
    )

    if servicios_disponibles:

        print("\nServicios que cubren directamente el recorrido:")
        print("-" * 50)

        for servicio in servicios_disponibles:
            print(f"- {servicio}")

    return servicios_disponibles

def encontrar_transbordos(ruta, servicios_ruta):
    """
    Identifica los puntos donde cambia el servicio
    durante el recorrido.
    """

    transbordos = []

    if len(servicios_ruta) <= 1:
        return transbordos

    servicio_anterior = servicios_ruta[0]

    for i in range(1, len(ruta)):

        estacion_anterior = ruta[i - 1]
        estacion_actual = ruta[i]

        servicios_tramo = obtener_servicios_tramo(
            estacion_anterior,
            estacion_actual
        )

        if servicio_anterior not in servicios_tramo:

            if i - 1 < len(ruta):

                transbordos.append(
                    {
                        "estacion": estacion_anterior,
                        "servicio_anterior": servicio_anterior,
                        "servicio_nuevo": servicios_tramo[0]
                        if servicios_tramo
                        else "Conexión"
                    }
                )

                servicio_anterior = (
                    servicios_tramo[0]
                    if servicios_tramo
                    else servicio_anterior
                )

    return transbordos


# ==========================================
# EJECUTAR SISTEMA
# ==========================================

def ejecutar_sistema():

    print("=" * 60)
    print("        SISTEMA INTELIGENTE DE RUTAS")
    print("        Transporte Masivo")
    print("=" * 60)

    mostrar_estaciones()

    # --------------------------------------
    # ORIGEN
    # --------------------------------------

    origen_ingresado = input(
        "\nIngrese la estación de origen: "
    )

    # --------------------------------------
    # DESTINO
    # --------------------------------------

    destino_ingresado = input(
        "Ingrese la estación de destino: "
    )

    # --------------------------------------
    # NORMALIZAR NOMBRES
    # --------------------------------------

    origen = buscar_nombre_estacion(
        origen_ingresado
    )

    destino = buscar_nombre_estacion(
        destino_ingresado
    )

    # --------------------------------------
    # VALIDAR ORIGEN
    # --------------------------------------

    if not estacion_valida(origen):

        print(
            f"\nError: '{origen_ingresado}' "
            "no es una estación válida."
        )

        return

    # --------------------------------------
    # VALIDAR DESTINO
    # --------------------------------------

    if not estacion_valida(destino):

        print(
            f"\nError: '{destino_ingresado}' "
            "no es una estación válida."
        )

        return

    # --------------------------------------
    # MOSTRAR SERVICIOS DIRECTOS
    # --------------------------------------

    servicios_disponibles = mostrar_servicios(
        origen,
        destino
    )

    # --------------------------------------
    # BUSCAR RUTA CON A*
    # --------------------------------------

    ruta = buscar_ruta(
        origen,
        destino
    )

    # --------------------------------------
    # MOSTRAR RESULTADO
    # --------------------------------------

    if ruta:

     estaciones_ruta = ruta["ruta"]
     servicios_ruta = ruta["servicios"]
     cantidad_transbordos = ruta["transbordos"]
     
     transbordos = encontrar_transbordos(
        estaciones_ruta,
        servicios_ruta
    )

    print("\n")
    print("=" * 60)
    print("             RUTA ENCONTRADA")
    print("=" * 60)

    print(f"\nOrigen: {origen}")
    print(f"Destino: {destino}")

    print("\nRecorrido:")
    print("-" * 60)

    for numero, estacion in enumerate(
        estaciones_ruta,
        start=1
    ):
        print(f"{numero}. {estacion}")

    print("-" * 60)

    cantidad_estaciones = len(
        estaciones_ruta
    )

    cantidad_desplazamientos = (
        cantidad_estaciones - 1
    )

    tiempo_estimado = (
        calcular_tiempo_estimado(
            cantidad_desplazamientos
        )
    )

    print(
        f"Cantidad de estaciones: "
        f"{cantidad_estaciones}"
    )

    print(
        f"Cantidad de desplazamientos: "
        f"{cantidad_desplazamientos}"
    )

    print(
        f"Tiempo estimado: "
        f"{tiempo_estimado} minutos"
    )

    print(
        f"Cantidad de transbordos: "
        f"{cantidad_transbordos}"
    )

    print("\nServicios utilizados:")

    for servicio in servicios_ruta:
        print(f"- {servicio}")

    print("=" * 60)
    
    if transbordos:

        print("\nTransbordos:")

        for transbordo in transbordos:

            print(
                f"🔄 TRANSBORDO EN: "
                f"{transbordo['estacion']}"
            )

            print(
                f"   Servicio anterior: "
                f"{transbordo['servicio_anterior']}"
            )

            print(
                f"   Nuevo servicio: "
                f"{transbordo['servicio_nuevo']}"
            )

    


# ==========================================
# INICIO DEL PROGRAMA
# ==========================================

if __name__ == "__main__":
    ejecutar_sistema()
        


