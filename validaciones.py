from os import system
from datos import *
from helpers import *

def menu_validacion(opcion: str, minimo: int, maximo: int) -> bool:
    validado = False

    if len(opcion) == 1:
        if ord(opcion) > minimo and ord(opcion) < maximo:
            validado = True
    return validado

def usuario_nombre_validacion(usuario: str) -> bool:
    validado = False
    for i in range(len(datos_usuarios)):
        if usuario == datos_usuarios[i]:
            validado = True
            break
    return validado

def usuario_password_validacion(password: str) -> bool:
    validado = False
    for i in range(len(datos_passwords)):
        if password == datos_passwords[i]:
            validado = True
            break
    return validado

def usuario_validacion() -> list:
    intentos = 0
    system("cls")
    usuario = input("Ingrese su nombre de usuario: ")
    validacion = False
    validacion_usuario = False
    validacion_password = False
    validacion_usuario = usuario_nombre_validacion(usuario)
    while not validacion_usuario and intentos < 3:
        system("cls")
        print(Fore.RED + f"Error! Cantidad de intentos: {3 - intentos}"+ Style.RESET_ALL)
        usuario = input(Fore.YELLOW +"Nombre de usuario no encontrado, reingrese: ")
        validacion_usuario = usuario_nombre_validacion(usuario)
        intentos += 1
    if validacion_usuario:
        system("cls")
        print(Fore.BLUE + f"Bienvenido {palabra_normalizada(usuario)}!!"+ Style.RESET_ALL)
        intentos = 0
        password = input(Fore.YELLOW +"Por favor, ingrese su contrasña para continuar: ")
        validacion_password = usuario_password_validacion(password)
        while not validacion_password and intentos < 3:
            system("cls")
            print(Fore.RED +"Error, contraseña incorrecta!!")
            print(f"Cantidad de intentos: {3 - intentos}")
            password = input("Reingrese: "+ Style.RESET_ALL)
            validacion_password = usuario_password_validacion(password)
            intentos += 1
    if validacion_usuario and validacion_password:
        print(Fore.BLUE + f"Ingresando a la cuenta de {palabra_normalizada(usuario)}."+ Style.RESET_ALL)
        validacion = True
    else:
        system("cls")
        print(Fore.RED +"No se ha podido ingresar a la cuenta, volviendo al menu principal."+ Style.RESET_ALL)
    return [validacion, usuario]

def validacion_eleccion_profesional(profesionales: list) -> str:
    profesional_validado = False
    profesional_seleccionado = ""
    apellido_encontrado = False
    opcion_profesional_sn = input(Fore.YELLOW +"Ingrese el apellido o nombre del profesional: ")
    opcion_profesional = palabra_normalizada(opcion_profesional_sn)
    while not profesional_validado:
        opcion_incorrecta = True
        for i in range(len(profesionales)):
            apellido = ""
            for j in range(len(profesionales[i])):
                if ord(profesionales[i][j]) == 44:
                    break
                else:
                    apellido += profesionales[i][j]

            if opcion_profesional == apellido:
                profesional_seleccionado = profesionales[i]
                profesional_validado = True
                opcion_incorrecta = False
                apellido_encontrado = True
                break

        if not apellido_encontrado:
            for i in range(len(profesionales)):
                espacio_y_coma_listos = False
                nombre = ""
                for j in range(len(profesionales[i])):
                    if ord(profesionales[i][j]) == 44:
                        espacio_y_coma_listos = True
                    elif espacio_y_coma_listos and ord(profesionales[i][j]) != 32 and ord(profesionales[i][j]) != 44:
                        nombre += profesionales[i][j]

                if opcion_profesional == nombre:
                    profesional_seleccionado = profesionales[i]
                    profesional_validado = True
                    opcion_incorrecta = False
                    apellido_encontrado = True
                    break
        while opcion_incorrecta:
            system("cls")
            print(Fore.RED +"El profesional no existe:"+ Style.RESET_ALL)
            opcion = input(Fore.YELLOW +"1- Ingresar nuevo apellido/nombre\n2- Volver al menu\nIngresar opcion: "+ Style.RESET_ALL)
            if opcion == "1":
                system("cls")
                print(Fore.GREEN +f"{"VETERINARIOS":^48}"+ Style.RESET_ALL)
                veterinarios = profesionales
                normalizar_lista_str(veterinarios)
                for i in range(len(veterinarios)):
                    print(Fore.YELLOW + f"{i+1}- {veterinarios[i]}")
                opcion_profesional_sn = input("Reingrese el apellido o nombre de el profesional: ")
                opcion_profesional = palabra_normalizada(opcion_profesional_sn)
                opcion_incorrecta = False
            elif opcion == "2":
                opcion_incorrecta = False
                profesional_validado = True
            else:
                print(Fore.RED +"Ingrese una opcion correcta"+ Style.RESET_ALL)
    return [profesional_validado, profesional_seleccionado]

def validacion_servicio(servicios: list, precios: list) -> list:
    servicio_validado = False
    servicio_seleccionado = ""
    precio_servicio = 0
    system("cls")
    opcion_servicio = input("SERVICIOS\n1- Consulta general\n2- Vacunacion\n3- Control Post-quirurgico\n4- Volver al Menu\nIngrese el servicio a solicitar: ")
    while not servicio_validado:
        if len(opcion_servicio) <= 1 and (ord(opcion_servicio) > 48 and ord(opcion_servicio) < 52):
            servicio_seleccionado = servicios[int(opcion_servicio)-1]
            precio_servicio = precios[int(opcion_servicio)-1]
            servicio_validado = True
        elif len(opcion_servicio) <= 1 and ord(opcion_servicio) == 52:
            break
        else:
            system("cls")
            print(Fore.RED + "Error!, debe ingresar una opcion entre 1 y 4"+ Style.RESET_ALL)
            opcion_servicio = input(Fore.YELLOW + "1- Consulta general\n2- Vacunacion\n3- Control Post-quirurgico\n4- Volver al Menu\nIngrese el servicio a solicitar: ")


    return [servicio_validado, servicio_seleccionado, precio_servicio]


