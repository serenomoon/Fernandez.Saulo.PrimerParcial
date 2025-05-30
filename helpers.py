from datos import *
from colorama import Fore,Style

def crear_vector(contenido: any, dimension: int) -> list:
    """Crea un vector repitiendo el "contenido" en cada uno de los espacios defiinidos por "dimension"
    Args:
        contenido (any): Contenido que llenara los indices del array (Ej: None)
        dimension (int): Cantidad de indices o posiciones que tendra el array

    Returns:
        list: Devuelve una lista "cruda"
    """
    vector = [contenido] * dimension
    return vector

def agregar_valor_lista(lista: list, nuevo_valor):
    """Toma una lista, y crea una nueva con el tamaño de la ingresada + 1 y luego agrega todos los valores
    de la anterior, mas el nuevo valor


    Args:
        lista (list): Lista a "actualizar"
        nuevo_valor (_type_): Valor nuevo a insertar en la nueva lista

    Returns:
        _type_: Devuelve una nueva lista actualizada
    """
    nueva_lista = crear_vector(None, len(lista) + 1)
    for i in range(len(lista)):
        nueva_lista[i] = lista[i]
    nueva_lista[len(lista)] = nuevo_valor
    return nueva_lista

def palabra_normalizada(palabra: str) -> str:
    """Sustituye las primeras letras y las que vienen luego de un espacio por sus respectivas mayusculas

    Args:
        palabra (str): palabra a modificar

    Returns:
        str: palabla con mayusculas en el index 0 y luego de un espacio
    """
    palabra_modificada = ""
    espacio_encontrado = False
    for i in range(len(palabra)):
        if i == 0:
            palabra_modificada += chr(ord(palabra[i]) - 32)
        elif ord(palabra[i]) == 32:
            palabra_modificada += " " + chr(ord(palabra[i+1]) - 32)
            espacio_encontrado = True
        elif espacio_encontrado:
            espacio_encontrado = False
            continue
        else:
            palabra_modificada += palabra[i]
    return palabra_modificada

def normalizar_lista_str(datos: list) -> list:
    """Toma una lista de str (ej: nombres y apellidos) y los devuelve normalizados, 
    con sus mayusculas al comenzar el nombre/apellido

    Args:
        datos (list): lista de strs

    Returns:
        list: lista de strs normalizadas
    """
    lista_modificada = []
    for i in range(len(datos)):
            palabra_modificada = palabra_normalizada(datos[i])
            lista_modificada = agregar_valor_lista(lista_modificada, palabra_modificada)
    return lista_modificada

def ordenar_alfabeticamente(lista: list, extra: list = None) -> list:
    """Ordena alfabeticamente una lista, si hay un extra, lo ordena acorde a la primer lista

    Args:
        lista (list): lista a ordenar
        extra (list, optional): lista extra a ordenar. Defaults to None.

    Returns:
        list: una lista con 2 listas dentro: lista ordenada y lista extra/None
    """
    lista_ordenada = lista
    extra_ordenado = extra
    todo_odenado = None
    for i in range(len(lista_ordenada)-1):
        for j in range(i+1,len(lista_ordenada)):
            if lista_ordenada[i] > lista_ordenada[j]:
                auxiliar = lista_ordenada[j]
                lista_ordenada[j] = lista_ordenada[i]
                lista_ordenada[i] = auxiliar
    
                if extra != None:
                    auxiliar = extra_ordenado[j]
                    extra_ordenado[j] = extra_ordenado[i]
                    extra_ordenado[i] = auxiliar
    todo_odenado = lista_ordenada
    if extra != None:
        todo_odenado = [lista_ordenada, extra_ordenado]
    return todo_odenado

def añadir_turno(consulta: list, vacunacion: list, quirurgico: list, profesionales: list, servicios: list, pro_seleccionado: str, serv_seleccionado: str) -> list:
    """Añade un turno a consulta, vacunacion o quirurgico, dependiendo el servicio.
    Lo acomoda en la lista segun el indice del profesional

    Returns:
        _type_: lista con el turno sumado a los demas turnos
    """
    turno_añadido = []
    for i in range(len(profesionales)):
        for j in range(len(servicios)):
            if pro_seleccionado == palabra_normalizada(profesionales[i]) and serv_seleccionado == palabra_normalizada(servicios[j]):
                if j == 0:
                    turno_añadido = consulta
                elif j == 1:
                    turno_añadido = vacunacion
                elif j == 2:
                    turno_añadido = quirurgico
                for k in range(len(turno_añadido)):
                    turno_añadido[i] += 1
                    break
                break
    return turno_añadido

def turnos_totales_por_veterinario(profesionales: list, consulta: list, vacunacion: list, quirurgico: list) -> None:
    """Calcula la cantidad de turnos totales por profesional

    Args:
        profesionales (list): profesionales
        consulta (list): lista de consulta
        vacunacion (list): lista de vacunacion
        quirurgico (list): lista de post-quirurgico
    """
    print(Fore.GREEN +"TURNOS TOTALES POR PROFESIONAL")
    print(f"{"\nProfesional":<30}", end="")
    print("Turnos\n"+ Style.RESET_ALL)
    for i in range(len(profesionales)):
        nombre = profesionales[i]
        nombre_normalizado = palabra_normalizada(nombre)
        print(Fore.YELLOW +f"{nombre_normalizado:<30}", end="")
        print(f"{consulta[i]+vacunacion[i]+quirurgico[i]}")

def promedio_turnos_entre_veterinarios(profesionales: list, consulta: list, vacunacion: list, quirurgico: list):
    """Calcula el promedio de turnos por tipo de servicio entre todos los veterinarios

    Args:
        profesionales (list): lista de profesionales
        consulta (list): lista de consulta
        vacunacion (list): lista de vacunacion
        quirurgico (list): lista de post-quirurgico
    """
    print(Fore.GREEN +"PROMEDIO DE TURNOS")
    print(f"{"\nProfesional":<30}", end="")
    print(f"{"Consulta general":<20}", end="")
    print(f"{"Vacunacion":<14}", end="")
    print(f"{"Post-quirurgico"}"+ Style.RESET_ALL)
    for i in range(len(profesionales)):
        nombre = profesionales[i]
        nombre_normalizado = palabra_normalizada(nombre)
        print(Fore.YELLOW +f"{nombre_normalizado:<29}", end="")
        print(f"{consulta[i]:<20}", end="")
        print(f"{vacunacion[i]:<14}", end="")
        print(f"{quirurgico[i]}")

def recaudacion_total(precios: list, consulta: list, vacunacion: list, quirurgico: list) -> None:
    """Calcula la recaudacion total de la veterinaria

    Args:
        precios (list): lista de precios
        consulta (list): lista de consulta
        vacunacion (list): lista de vacunacion
        quirurgico (list): lista de post-quirurgico
    """
    total = 0
    for i in range(len(consulta)):
        total += consulta[i] * precios[0]
        total += vacunacion[i] * precios[1]
        total += quirurgico[i] * precios[2]
    print(Fore.GREEN +"TOTAL RECAUDADO\nClinica Veterinaria 'El Rope'"+ Style.RESET_ALL)
    print(Fore.YELLOW +f"$ {total}")

def ordenar_turnos(ordenamiento: list, lista_a_ordenar: list) -> list:
    """Ordena los turnos en base un array de numeros

    Args:
        ordenamiento (list): array con numeros dentro, cada uno equivale al indice a utilizar
        lista_a_ordenar (list): lista a ordenar

    Returns:
        list: lista ordenada
    """
    lista_nueva = [None for _ in range(len(lista_a_ordenar))]
    for i in range(len(ordenamiento)):
        lista_nueva[i] = lista_a_ordenar[ordenamiento[i]]
    return lista_nueva

def recaudacion_por_servicio(profesionales: list, precios: list, consulta: list, vacunacion: list, quirurgico: list) -> None:
    """Muestra lo recaudado por cada profesional

    Args:
        profesionales (list): lista de profesionales
        precios (list): lista de precios
        consulta (list): lista de consulta
        vacunacion (list): lista de vacunacion
        quirurgico (list): lista de post-quirurgico
    """
    profesionales_lista = normalizar_lista_str(profesionales)
    ordenamiento = [i for i in range(len(profesionales_lista))]
    ordenar_alfabeticamente(profesionales_lista, ordenamiento)
    consulta_ordenada = ordenar_turnos(ordenamiento, consulta)
    vacunacion_ordenada = ordenar_turnos(ordenamiento, vacunacion)
    quirurgico_ordenada = ordenar_turnos(ordenamiento, quirurgico)
    print(Fore.GREEN +"RECAUDACION POR PROFESIONAL")
    print(f"{"\nProfesional":<30}", end="")
    print("Recaudado\n"+ Style.RESET_ALL)
    for i in range(len(profesionales_lista)):
        print(Fore.YELLOW +f"{profesionales_lista[i]:<29}", end="")
        print(f"$ {consulta_ordenada[i]*precios[0] + vacunacion_ordenada[i]*precios[1] + quirurgico_ordenada[i]*precios[2]}")

def porcentaje_por_servicio(servicios:list, consulta: list, vacunacion: list, quirurgico: list) -> None:
    """Muestra el porcentaje de cada tipo de servicio respecto al total general de turnos

    Args:
        servicios (list): lista de servicios
        consulta (list): lista de consulta
        vacunacion (list): lista de vacunacion
        quirurgico (list): lista de post-quirurgico
    """
    total_servicios = 0
    total_por_servicio = [0 for _ in range(len(servicios))]
    for i in range(len(consulta)):
        total_servicios += consulta[i] + vacunacion[i] + quirurgico[i]
        total_por_servicio[0] += consulta[i]
        total_por_servicio[1] += vacunacion[i]
        total_por_servicio[2] += quirurgico[i]
    print(Fore.GREEN +"PORCENTAJE POR SERVICIO")
    print(f"{"\nServicios":<30}", end="")
    print("Porcentaje de turnos\n"+ Style.RESET_ALL)
    for i in range(len(servicios)):
        print(Fore.YELLOW +f"{servicios[i]:<29}", end="")
        if total_servicios != 0:
            porcentaje = (total_por_servicio[i]) * 100 / total_servicios
        else:
            porcentaje = 0.0
        print(f"% {porcentaje}")

def profesional_menos_turnos(profesionales: list, consulta: list, vacunacion: list, quirurgico: list) -> None:
    """Muestra el veterinario con menor cantidad total de turnos

    Args:
        profesionales (list): lista de profesionales
        consulta (list): lista de consulta
        vacunacion (list): lista de vacunacion
        quirurgico (list): lista de post-quirurgico
    """
    profesional_sin_laburo = ""
    cantidad_menor_turnos = 0
    cantidad_turnos = 0
    for i in range(len(profesionales)):
        cantidad_turnos = consulta[i] + vacunacion[i] + quirurgico[i]
        if cantidad_menor_turnos > cantidad_turnos or i == 0:
            cantidad_menor_turnos = cantidad_turnos
            profesional_sin_laburo = profesionales[i]
    print(Fore.GREEN +"PROFESIONAL CON MENOS TURNOS")
    print(f"{"\nProfesional":<30}", end="")
    print("Cantidad de turnos\n"+ Style.RESET_ALL)
    print(Fore.YELLOW +f"{palabra_normalizada(profesional_sin_laburo):<29}", end="")
    print(f"{cantidad_menor_turnos}")

def porcentaje_turnos_por_profesional(profesionales: list, consulta: list, vacunacion: list, quirurgico: list):
    """Muestra el porcentaje de turnos por veterinario respecto al total general

    Args:
        profesionales (list): lista de profesionales
        consulta (list): lista de consulta
        vacunacion (list): lista de vacunacion
        quirurgico (list): lista de post-quirurgico
    """
    total_turnos = 0
    for i in range(len(profesionales)):
        total_turnos += consulta[i] + vacunacion[i] + quirurgico[i]
    print(Fore.GREEN +"PORCENTAJE TURNOS POR PROFESIONAL")
    print(f"{"\nProfesional":<30}", end="")
    print("Porcentaje\n"+ Style.RESET_ALL)
    for i in range(len(profesionales)):
        print(Fore.YELLOW +f"{palabra_normalizada(profesionales[i]):<29}", end="")
        if total_turnos != 0:
            porcentaje = (consulta[i]+ vacunacion[i] + quirurgico[i]) * 100 / total_turnos
        else:
            porcentaje = 0.0
        print(f"% {porcentaje}")

def servicio_mas_solicitado(profesionales: list, servicios:list, consulta: list, vacunacion: list, quirurgico: list):
    """Muestra el servicio/s más solicitado/s por cada veterinario

    Args:
        profesionales (list): lista de profesionales
        servicios (list): lista de servicios
        consulta (list): lista de consulta
        vacunacion (list): lista de vacunacion
        quirurgico (list): lista de post-quirurgico
    """
    print(Fore.GREEN +"SERVICIO MAS SOLICITADO")
    print(f"{"\nProfesional":<30}", end="")
    print("Servicio\n"+ Style.RESET_ALL)
    for i in range(len(profesionales)):
        servicio_mas_solicitado = "no hay"
        if consulta[i] > vacunacion[i] and consulta[i] > quirurgico[i]:
            servicio_mas_solicitado = servicios[0]
        elif vacunacion[i] > quirurgico[i]:
            servicio_mas_solicitado = servicios[1]
        elif vacunacion[i] < quirurgico[i]:
            servicio_mas_solicitado = servicios[2]
        print(Fore.YELLOW +f"{palabra_normalizada(profesionales[i]):<29}", end="")
        print(f"{palabra_normalizada(servicio_mas_solicitado)}")


def servicio_mas_recaudado(servicios: list, precios:list, consulta: list, vacunacion: list, quirurgico: list) -> None:
    total_consulta = 0 
    total_vacunacion = 0 
    total_quirurgico = 0 
    for i in range(len(consulta)):
        total_consulta += consulta[i] * precios[0]
        total_vacunacion += vacunacion[i] * precios[1]
        total_quirurgico += quirurgico[i] * precios[2]
    print(Fore.GREEN +"SERVICIO CON MAS RECAUDACION")
    print(f"{"\nServicio":<30}", end="")
    print("Recaudado\n"+ Style.RESET_ALL)
    if total_consulta > total_vacunacion and total_consulta > total_quirurgico:
        print(Fore.YELLOW +f"{palabra_normalizada(servicios[0]):<29}", end="")
        print(f"$ {total_consulta}")
    elif total_vacunacion > total_quirurgico:
        print(Fore.YELLOW +f"{palabra_normalizada(servicios[1]):<29}", end="")
        print(f"$ {total_vacunacion}")
    elif total_quirurgico > total_vacunacion:
        print(Fore.YELLOW +f"{palabra_normalizada(servicios[2]):<29}", end="")
        print(f"$ {total_quirurgico}")
    else:
        print(Fore.RED +"No hay ningun servicio activo")

def porcentaje_turnos_alfabeticamente(profesional: list, consulta: list, vacunacion: list, quirurgico: list) -> None:
    profesionales_sn = profesional
    ordenamiento = [i for i in range(len(profesional))]
    total_turnos = 0
    consulta_ordenada = consulta
    vacunacion_ordenada = vacunacion
    quirurgico_ordenada = quirurgico
    ordenar_alfabeticamente(profesionales_sn, ordenamiento)
    print(Fore.GREEN +"PORCENTAJE DE TURNOS")
    print(f"{"\nProfesional":<30}", end="")
    print("Porcentaje\n"+ Style.RESET_ALL)
    for i in range(len(ordenamiento)):
        total_turnos += consulta[i] + vacunacion[i] + quirurgico[i]
        consulta_ordenada[i] = consulta_ordenada[ordenamiento[i]]
        vacunacion_ordenada[i] = vacunacion_ordenada[ordenamiento[i]]
        quirurgico_ordenada[i] = quirurgico_ordenada[ordenamiento[i]]
    for i in range(len(profesionales_sn)):
        print(Fore.YELLOW +f"{palabra_normalizada(profesionales_sn[i]):<29}", end="")
        if total_turnos != 0:
            print(f"% {(consulta_ordenada[i] + vacunacion_ordenada[i] + quirurgico_ordenada[i]) * 100 / total_turnos}")
        else:
            print("No hay turnos")
    
    
    
