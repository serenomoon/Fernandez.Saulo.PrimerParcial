import sys
from os import system
from validaciones import *
from opciones import *
from helpers import *
from datos import *
from colorama import Fore,Style


def main() -> None:
    menu_abierto = True
    opcion_validada = False
    usuario_temp = ""
    usuario_logueado = False
    cantidad_turnos_consulta = [0 for _ in range(len(datos_profesionales))]
    cantidad_turnos_vacunacion = [0 for _ in range(len(datos_profesionales))]
    cantidad_turnos_quirurgico = [0 for _ in range(len(datos_profesionales))]
    system("cls")
    while menu_abierto:
        print(Fore.GREEN +"Bienvenido a Clinica Veterinaria 'El Rope'"+ Style.RESET_ALL)
        if usuario_logueado:
            print(Fore.BLUE +f"Hola de nuevo {palabra_normalizada(usuario_temp)}!"+ Style.RESET_ALL)
        opcion = input(Fore.YELLOW+"MENU DE OPCIONES\n1- Ingresar con usuario\n2- Registrar turno\n3- Visualizar Datos\n4- Consultas\n5- Salir\nIngrese una opcion: ")
        opcion_validada = menu_validacion(opcion, 48, 54)
        if opcion_validada:
            match opcion:
                case "1":
                    if usuario_logueado:
                        print("Ya se encuentra logueado")
                    else:
                        usuario_dato = opcion_1()
                        if usuario_dato[0]:
                            usuario_logueado = usuario_dato[0]
                            usuario_temp = usuario_dato[1]
                case "2":
                    if usuario_logueado:
                        system("cls")
                        nuevo_turno = opcion_2()
                        if nuevo_turno[0]:
                            system("cls")
                            print(f"Profesional: {nuevo_turno[1]}")
                            print(f"Servicio: {nuevo_turno[2]}")
                            print(f"Precio: ${nuevo_turno[3]}")
                            for i in range(len(datos_servicios)):
                                if nuevo_turno[2] == palabra_normalizada(datos_servicios[i]):
                                    if i == 0:
                                        cantidad_turnos_consulta = añadir_turno(cantidad_turnos_consulta, cantidad_turnos_vacunacion, cantidad_turnos_quirurgico, datos_profesionales, datos_servicios, nuevo_turno[1], nuevo_turno[2])
                                    elif i == 1:
                                        cantidad_turnos_vacunacion = añadir_turno(cantidad_turnos_consulta, cantidad_turnos_vacunacion, cantidad_turnos_quirurgico, datos_profesionales, datos_servicios, nuevo_turno[1], nuevo_turno[2])
                                    elif i == 2:
                                        cantidad_turnos_quirurgico = añadir_turno(cantidad_turnos_consulta, cantidad_turnos_vacunacion, cantidad_turnos_quirurgico, datos_profesionales, datos_servicios, nuevo_turno[1], nuevo_turno[2])
                                    break
                    else:
                        system("cls")
                        print("Debe loguearse para usar el servicio.")
                case "3":
                    system("cls")
                    turnos_totales = 0
                    for i in range(len(datos_profesionales)):
                        turnos_totales += cantidad_turnos_consulta[i] + cantidad_turnos_vacunacion[i] + cantidad_turnos_quirurgico[i]
                    opcion_3(turnos_totales)
                case "4":
                    system("cls")
                    opcion_4(cantidad_turnos_consulta, cantidad_turnos_vacunacion, cantidad_turnos_quirurgico)
                case "5":
                    menu_abierto = opcion_5()
            system("pause")
            system("cls")
        else:
            print(Fore.RED +"Debe elegir una opcion entre 1 y 5."+ Style.RESET_ALL)
            system("pause")
            system("cls")

if __name__ == "__main__":
    sys.exit(main())