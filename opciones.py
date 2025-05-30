from os import system
from validaciones import *
from datos import *
from colorama import Fore,Style

def opcion_1():
    return usuario_validacion()


def opcion_2():
    turno_validado = False
    turno = [turno_validado]
    print(Fore.GREEN +f"{"VETERINARIOS":^48}"+ Style.RESET_ALL)
    profesionales = normalizar_lista_str(datos_profesionales)
    for i in range(len(profesionales)):
        print(Fore.YELLOW +f"{i+1}- {profesionales[i]}")
    pro_validado = validacion_eleccion_profesional(profesionales)
    if pro_validado[0] and pro_validado[1] != "":
        system("cls")
        print(f"Veterinario seleccionado: {pro_validado[1]}")
        system("pause")
        serv_validado = validacion_servicio(datos_servicios, datos_precios)
        if serv_validado[0]:
            turno_validado = True
            serv_normalizado = palabra_normalizada(serv_validado[1])
            turno = [turno_validado, pro_validado[1], serv_normalizado, serv_validado[2]]
    else:
        system("cls")
        print(Fore.YELLOW +"Volviendo al Menu...")
    return turno


def opcion_3(turnos: list) -> None:
    print(Fore.GREEN +f"{"VETERINARIOS":^48}"+ Style.RESET_ALL)
    profesionales_sin_normalizar = datos_profesionales
    profesionales = ordenar_alfabeticamente(normalizar_lista_str(profesionales_sin_normalizar))
    for i in range(len(profesionales)):
        if i % 2 == 0:
            print(Fore.YELLOW +f"{profesionales[i]:<30}", end="")
        else:
            print(f"{profesionales[i]:<30}")
    print(Fore.GREEN +f"{"\nSERVICIOS":<30}", end="")
    print("PRECIOS"+ Style.RESET_ALL)
    for i in range(len(datos_precios)):
         print(Fore.YELLOW +f"{palabra_normalizada(datos_servicios[i]):<29}", end="")
         print(f"${datos_precios[i]:<10}")
    print(Fore.GREEN +f"{"\nTURNOS RESERVADOS":<30}", end=""+ Style.RESET_ALL)
    print(Fore.YELLOW +f"{turnos}\n")
    

def opcion_4(consulta:list , vacunacion: list, quirurgico: list):
    submenu = True
    while submenu:
        system("cls")
        print(Fore.GREEN +"CONSULTAS"+ Style.RESET_ALL)
        opcion_consulta = input(Fore.YELLOW +"1- Listado con la cantidad total de turnos reservados por cada veterinario\n" \
        "2- Promedio de turnos por tipo de servicio entre todos los veterinarios\n" \
        "3- Recaudación total acumulada por todos los veterinarios\n" \
        "4- Veterinarios ordenados alfabéticamente de la A-Z junto al total que recaudó en concepto de servicios\n" \
        "5- Porcentaje de cada tipo de servicio respecto al total general de turnos\n" \
        "6- Veterinario con menor cantidad total de turnos atendidos\n" \
        "7- Porcentaje de turnos por veterinario respecto al total general\n" \
        "8- Servicio/s más solicitado/s por cada veterinario\n" \
        "9- El servicio que más recaudó en promedio.\n" \
        "10- Porcentaje de turnos por veterinario respecto del total general, junto con su nombre. Ordenados alfabéticamente\n" \
        "11- Volver al Menu\n" \
        "Ingrese una opcion: "
    )
        opcion_validada = menu_validacion(opcion_consulta, 48, 58)
        if opcion_validada:
            system("cls")
            match opcion_consulta:
                case "1":
                    turnos_totales_por_veterinario(datos_profesionales, consulta, vacunacion, quirurgico)
                    system("pause")
                case "2":
                    promedio_turnos_entre_veterinarios(datos_profesionales, consulta, vacunacion, quirurgico)
                    system("pause")
                case "3":
                    recaudacion_total(datos_precios, consulta, vacunacion, quirurgico)
                    system("pause")
                case "4":
                    recaudacion_por_servicio(datos_profesionales, datos_precios, consulta, vacunacion, quirurgico)
                    system("pause")
                case "5":
                    porcentaje_por_servicio(datos_servicios, consulta, vacunacion, quirurgico)
                    system("pause")
                case "6":
                    profesional_menos_turnos(datos_profesionales, consulta, vacunacion, quirurgico)
                    system("pause")
                case "7":
                    porcentaje_turnos_por_profesional(datos_profesionales, consulta, vacunacion, quirurgico)
                    system("pause")
                case "8":
                    servicio_mas_solicitado(datos_profesionales, datos_servicios, consulta, vacunacion, quirurgico)
                    system("pause")
                case "9":
                    servicio_mas_recaudado(datos_servicios, datos_precios, consulta, vacunacion, quirurgico)
                    system("pause")
                case "10":
                    porcentaje_turnos_alfabeticamente(datos_profesionales, consulta, vacunacion, quirurgico)
                    system("pause")
                case "11":
                    print("Volviendo al Menu...")
                    submenu = False
        else:
            print(Fore.RED + "Debe elegir una opcion entre 1 y 9."+ Style.RESET_ALL)
            system("pause")
            system("cls")


def opcion_5():
    system("cls")
    print("Saliendo del programa..."+ Style.RESET_ALL)
    return False