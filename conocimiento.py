# ==========================================
# BASE DE CONOCIMIENTO
# SISTEMA INTELIGENTE DE RUTAS
# ==========================================


# ==========================================
# RECORRIDOS DE LOS SERVICIOS
# ==========================================

servicios = {

    # --------------------------------------
    # RUTA 2
    # Portal 20 de Julio -> Museo Nacional
    # --------------------------------------
    "Ruta 2": [
        "Portal 20 de Julio",
        "Country Sur",
        "Avenida Primero de Mayo",
        "Bicentenario",
        "San Victorino",
        "Las Nieves",
        "San Diego",
        "Museo Nacional"
    ],


    # --------------------------------------
    # D81
    # Portal 20 de Julio -> Museo Nacional
    # --------------------------------------
    "D81": [
        "Portal 20 de Julio",
        "Country Sur",
        "Avenida Primero de Mayo",
        "Bicentenario",
        "San Victorino",
        "Museo Nacional"
    ],


    # --------------------------------------
    # F51
    # Portal Américas -> Museo Nacional
    # --------------------------------------
    "F51": [
        "Portal Américas",
        "Patio Bonito",
        "Biblioteca Tintal",
        "Banderas",
        "Mandalay",
        "Av Américas - Av. Boyacá",
        "Marsella",
        "Pradera - Plaza Central",
        "Distrito Grafiti",
        "Ricaurte",
        "Avenida Jiménez",
        "Las Nieves",
        "San Diego",
        "Museo Nacional"
    ],


    # --------------------------------------
    # B10
    # Portal 80 -> Portal Norte
    # --------------------------------------
    "B10": [
        "Portal 80",
        "Carrera 90",
        "Avenida Cali",
        "Granja - cra 77",
        "Boyacá",
        "Avenida 68",
        "Carrera 53",
        "Carrera 47",
        "Calle 85 - Gato Dumas",
        "Calle 100 - Marketmedios",
        "Alcalá - Colegio S. Tomás Dominicos",
        "Calle 146",
        "Mazurén",
        "Toberín",
        "Portal Norte - Unicervantes"
    ],


    # --------------------------------------
    # L10
    # Portal El Dorado -> Portal 20 de Julio
    # --------------------------------------
    "L10": [
        "Portal El Dorado",
        "Modelia",
        "Normandia",
        "Salitre El Greco - Vive Claro",
        "CAN - British Council",
        "Gobernacion",
        "Ciudad Universitaria",
        "Centro Memoria",
        "Las Nieves",
        "San Victorino",
        "Bicentenario",
        "Estación San Bernardo",
        "Ciudad Jardín - UAN",
        "Av. Primero de Mayo",
        "Portal 20 de Julio"
    ],


    # --------------------------------------
    # G11
    # Terminal -> Portal Sur
    # --------------------------------------
    "G11": [
        "Terminal",
        "Calle 187",
        "Toberín",
        "Calle 146",
        "Calle 106",
        "Virrey - Cendiatra",
        "Calle 85 - Gato Dumas",
        "Héroes - Colmena Seguros",
        "Escuela Militar",
        "Campin - UAN",
        "Paloquemao",
        "Ricaurte",
        "Santa Isabel",
        "NQS Calle 30 SUR",
        "Alquería",
        "C.C Paseo Villa Del Rio - Madelena",
        "Portal Sur - JFK Coop. Financiera"
    ],


    # --------------------------------------
    # M83
    # Portal Usme -> Museo Nacional
    # --------------------------------------
    "M83": [
        "Portal Usme",
        "Danubio",
        "Consuelo",
        "Quiroga",
        "Av. Primero de Mayo",
        "Policarpa",
        "Bicentenario",
        "San Victorino",
        "San Diego",
        "Museo Nacional"
    ]
}


# ==========================================
# REGLAS LÓGICAS
# ==========================================

def servicio_cubre_tramo(servicio, origen, destino):
    """
    Determina si un servicio permite viajar
    desde el origen hasta el destino.
    """

    recorrido = servicios.get(servicio, [])

    if origen not in recorrido or destino not in recorrido:
        return False

    posicion_origen = recorrido.index(origen)
    posicion_destino = recorrido.index(destino)

    return posicion_origen < posicion_destino


def obtener_servicios(origen, destino):
    """
    Obtiene todos los servicios que permiten
    viajar directamente entre el origen y destino.
    """

    servicios_disponibles = []

    for servicio in servicios:

        if servicio_cubre_tramo(
            servicio,
            origen,
            destino
        ):
            servicios_disponibles.append(servicio)

    return servicios_disponibles


def obtener_recorrido(servicio, origen, destino):
    """
    Obtiene las estaciones comprendidas
    entre el origen y el destino.
    """

    recorrido = servicios.get(servicio, [])

    if origen not in recorrido or destino not in recorrido:
        return []

    inicio = recorrido.index(origen)
    fin = recorrido.index(destino)

    return recorrido[inicio:fin + 1]


# ==========================================
# ESTACIONES DISPONIBLES
# ==========================================

def estaciones_disponibles():
    """
    Devuelve todas las estaciones registradas
    en la base de conocimiento.
    """

    estaciones = set()

    for recorrido in servicios.values():
        estaciones.update(recorrido)

    return sorted(estaciones)


def estacion_valida(estacion):
    """
    Verifica si una estación existe
    en la base de conocimiento.
    """

    return estacion in estaciones_disponibles()


# ==========================================
# ESTIMACIÓN DEL TIEMPO
# ==========================================

TIEMPO_POR_DESPLAZAMIENTO = 3


def calcular_tiempo_estimado(cantidad_desplazamientos):
    """
    Calcula un tiempo aproximado.

    Para este proyecto académico se estiman
    3 minutos por desplazamiento.

    Este valor NO representa el tiempo real
    de TransMilenio.
    """

    return cantidad_desplazamientos * TIEMPO_POR_DESPLAZAMIENTO