from collections import namedtuple

EstacionSevici = namedtuple("EstacionSevici", 
    "nombre, direccion, latitud, longitud, capacidad, puestos_libres, bicicletas_disponibles")

def selecciona_color(estacion:EstacionSevici) -> str:
    if estacion.capacidad==0:
        return "gray"
    disponibilidad=estacion.bicicletas_disponibles / estacion.capacidad
    if disponibilidad==0:
        return "gray"
    elif 0<disponibilidad<1/3:
        return "red"
    elif disponibilidad<2/3 or disponibilidad==1/3:
        return "orange"
    elif disponibilidad>=2/3:
        return "green"



def calcula_estadisticas(estaciones: list[EstacionSevici]) -> tuple[int, int, float, int]:
    """
    Calcula estadísticas de las estaciones.
    Parametros:
    estaciones: lista de EstacionSevici
    Devuelve:
    tupla con (total de bicicletas libres, total de capacidad, porcentaje de ocupación, total de estaciones)
    """
    bicicletas_libres=0
    total_capacidad=0
    total_estaciones=0
    porcentaje_ocupacion=0
    for c in estaciones:
        bicicletas_libres+=c.bicicletas_disponibles
        total_capacidad+=c.capacidad
        total_estaciones+=1
    porcentaje_ocupacion=((total_capacidad-bicicletas_libres)/total_capacidad)*100

    return bicicletas_libres,total_capacidad,porcentaje_ocupacion,total_estaciones



def busca_estaciones_direccion(estaciones: list[EstacionSevici], direccion_parcial: str) -> list[EstacionSevici]:
    """
    Busca las estaciones que contengan en su dirección (subcadena, sin distinguir mayúsculas/minúsculas) la dirección parcial dada.    

    Parametros:
    estaciones: lista de EstacionSevici
    direccion_parcial: subcadena a buscar en la dirección de las estaciones

    Devuelve:
    lista de EstacionSevici que cumplen el criterio
    """
    estaciones_parciales=[]
    for c in estaciones: 
        if direccion_parcial.lower() in c.direccion.lower():
            estaciones_parciales.append(c)
    return estaciones_parciales

def busca_estaciones_con_disponibilidad(estaciones:list[EstacionSevici], min_disponibilidad: float = 0.5) -> list[EstacionSevici]:
    """
    Devuelve una lista de EstacionSevici con al menos el porcentaje mínimo de bicicletas disponible
    indicado.

    Parametros:
    estaciones: lista de EstacionSevici
    min_disponibilidad: porcentaje mínimo de bicicletas disponibles (0.0 a 1.0)
    
    Devuelve:
    lista de EstacionSevici
    """
    estaciones_disponibilidad=[]
    for c in estaciones:
        if c.bicicletas_disponibles==0:
            return "No hay bicicletas disponibles"
        if c.bicicletas_disponibles / c.capacidad >= min_disponibilidad:
            estaciones_disponibilidad.append(c)
    return estaciones_disponibilidad


    # TODO: Ejercicio 4
    

def calcula_distancia(p1: tuple[float, float], p2: tuple[float, float]) -> float:
    """
    Calcula la distancia euclídea entre dos puntos (latitud, longitud).

    Parámetros:
    p1: tupla (latitud, longitud) del primer punto
    p2: tupla (latitud, longitud) del segundo punto

    Devuelve:
    float: distancia euclídea entre los dos puntos
    """
    # TODO: Ejercicio 5
    pass

def busca_estacion_mas_cercana(estaciones:list[EstacionSevici], punto:tuple[float, float]) -> EstacionSevici | None:
    """
    Devuelve la estación más cercana al punto dado (latitud, longitud) que tenga al menos una bicicleta disponible.
    
    Parametros:
    estaciones: lista de EstacionSevici
    punto: tupla (latitud, longitud)

    Devuelve:
    EstacionSevici más cercana con al menos una bicicleta disponible, o None si no hay ninguna.
    """ 
    # TODO: Ejercicio 5
    return None

def calcula_ruta(estaciones:list[EstacionSevici], origen:tuple[float, float], destino:tuple[float, float]) -> tuple[EstacionSevici | None, EstacionSevici | None]   :
    """
    Devuelve las estaciones más cercanas al punto de origen y destino dados, que tengan al menos una bicicleta disponible.

    Parametros: 
    estaciones: lista de EstacionSevici
    origen: tupla (latitud, longitud) del punto de origen
    destino: tupla (latitud, longitud) del punto de destino

    Devuelve:
    tupla con (estacion_origen, estacion_destino)
    """
    # TODO: Ejercicio 5
    pass

