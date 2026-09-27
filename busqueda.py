# ==========================================
# ALGORITMO DE BÚSQUEDA A*
# ==========================================

from conocimiento import servicios


# ==========================================
# FUNCIÓN HEURÍSTICA
# ==========================================

def heuristica(estacion_actual, destino):
    """
    Función heurística utilizada por A*.

    Estima el costo restante entre la estación
    actual y el destino.

    Se utiliza una estimación conservadora:
    - 0 si ya estamos en el destino.
    - 1 si todavía falta llegar al destino.

    Esta estimación evita sobreestimar el costo
    restante cuando existen diferentes servicios
    y posibles transbordos.
    """

    if estacion_actual == destino:
        return 0

    return 1


# ==========================================
# OBTENER CONEXIONES
# ==========================================

def obtener_vecinos(estacion):
    """
    Obtiene las estaciones conectadas directamente
    con la estación actual según los servicios
    registrados en la base de conocimiento.
    """

    vecinos = set()

    for recorrido in servicios.values():

        if estacion in recorrido:

            posicion = recorrido.index(estacion)

            # Estación anterior
            if posicion > 0:
                vecinos.add(recorrido[posicion - 1])

            # Estación siguiente
            if posicion < len(recorrido) - 1:
                vecinos.add(recorrido[posicion + 1])

    return list(vecinos)

def obtener_servicios_tramo(origen, destino):
    """
    Determina qué servicios conectan directamente
    dos estaciones consecutivas.

    Se consideran ambas direcciones del recorrido,
    ya que un servicio puede utilizarse en sentido
    contrario al orden almacenado en la base.
    """

    servicios_tramo = []

    for nombre_servicio, recorrido in servicios.items():

        if origen in recorrido and destino in recorrido:

            posicion_origen = recorrido.index(origen)
            posicion_destino = recorrido.index(destino)

            diferencia = abs(
                posicion_destino - posicion_origen
            )

            # Las estaciones son consecutivas
            if diferencia == 1:
                servicios_tramo.append(
                    nombre_servicio
                )

    return servicios_tramo


# ==========================================
# ALGORITMO A*
# ==========================================

def buscar_ruta(origen, destino):
    """
    Algoritmo A* que encuentra una ruta y conserva
    información sobre los servicios utilizados.
    """

    if origen == destino:
        return {
            "ruta": [origen],
            "servicios": [],
            "transbordos": 0
        }
        
    # Verificar primero si existe un servicio
    # que cubra todo el recorrido directamente.
    servicios_directos = []

    for nombre_servicio, recorrido in servicios.items():

        if origen in recorrido and destino in recorrido:

            posicion_origen = recorrido.index(origen)
            posicion_destino = recorrido.index(destino)

            if posicion_origen < posicion_destino:

                tramo = recorrido[
                    posicion_origen:posicion_destino + 1
                ]

                servicios_directos.append(
                    (
                        nombre_servicio,
                        tramo
                    )
                )

    # Si existen servicios directos, seleccionamos
    # el que tenga menos desplazamientos.
    if servicios_directos:

        servicios_directos.sort(
            key=lambda elemento: len(elemento[1])
        )

        servicio_elegido, recorrido_elegido = (
            servicios_directos[0]
        )

        return {
            "ruta": recorrido_elegido,
            "servicios": [servicio_elegido],
            "transbordos": 0
        }

    pendientes = [
        (
            origen,
            [origen],
            [],
            0
        )
    ]

    costos = {
        origen: 0
    }

    while pendientes:

        pendientes.sort(
            key=lambda elemento:
            elemento[3] + heuristica(
                elemento[0],
                destino
            )
        )

        (
            estacion_actual,
            ruta,
            servicios_ruta,
            costo_actual
        ) = pendientes.pop(0)

        if estacion_actual == destino:

            servicios_usados = []

            for servicio in servicios_ruta:

                if not servicios_usados:
                    servicios_usados.append(servicio)

                elif servicios_usados[-1] != servicio:
                    servicios_usados.append(servicio)

            transbordos = max(
                0,
                len(servicios_usados) - 1
            )

            return {
                "ruta": ruta,
                "servicios": servicios_usados,
                "transbordos": transbordos
            }

        for siguiente in obtener_vecinos(
            estacion_actual
        ):

            nuevo_costo = costo_actual + 1

            if (
                siguiente not in costos
                or nuevo_costo < costos[siguiente]
            ):

                servicios_tramo = (
                    obtener_servicios_tramo(
                        estacion_actual,
                        siguiente
                    )
                )

                if servicios_tramo:

                    servicio = servicios_tramo[0]

                else:

                    servicio = "Conexión"

                costos[siguiente] = nuevo_costo

                nueva_ruta = (
                    ruta + [siguiente]
                )

                nuevos_servicios = (
                    servicios_ruta + [servicio]
                )

                pendientes.append(
                    (
                        siguiente,
                        nueva_ruta,
                        nuevos_servicios,
                        nuevo_costo
                    )
                )

    return None