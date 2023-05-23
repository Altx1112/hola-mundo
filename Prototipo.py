import msvcrt
import json
import os
import time

try:
    from colorama import Fore, Back, Cursor, init

except ModuleNotFoundError:
    print("¡Hola! Esperamos que disfrutes y aprendas con el programa de <HOLA MUNDO>.\n")
    print("¡Pero antes de entrar, tu primer tarea será instalar la") 
    print("librería colorama para que el programa muestre colores.\n")
    print("Para hacerlo sigue las instrucciones:\n")
    print("[1] Abre la consola de comandos de Windows (Win + R, luego escribir cmd)\n")
    print("[2] Ingresa el comando tal cual pip install colorama\n")
    print("[3] Espera a que se complete y listo\n")
    print("[4] ¡Haz click en cualquier tecla y reinicia el programa!")
    msvcrt.getch()


def cuadro(): #Cuadro que se ve en pantalla con las instrucciones de uso
    linea = "____________________________________________________________________"
    y = 3
    print(f"{Cursor.POS(24, 2)}{linea}")
    for i in range(25):
        print(f"{Cursor.POS(23, y)}|{Cursor.POS(92, y)}|")
        y += 1

    print(f"{Cursor.POS(24, y-1)}{linea}")
    print(f"{Cursor.POS(18, y+1)}Mover cursor: Arriba / Abajo | Entrar: Enter | Cambiar Pág: Izquierda / Derecha")

def ver_leccion(lenguaje, leccion, id): #Imprime la lección en base a los archivos de texto
    with open("cuentas.json", "r") as datos: 
        datos_json = json.load(datos)
        nombre_usuario = datos_json["cuentas"][id]["nombre"]
        datos.close()

    match lenguaje: #Nos da la ruta dependiendo de la lección que querramos ver y las respuestas de cada práctica
        case 0:
            ruta = "lecciones/introduccion/"

        case 1:
            ruta = "lecciones/Python/"
            ruta_practicas = "practicas/Python/"
            match leccion:
                case 0:
                    respuesta = 0

                case 1:
                    respuesta = 3

                case 2:
                    respuesta = 0

                case 3:
                    respuesta = 2

                case 4:
                    respuesta = 0

                case 5:
                    respuesta = 3
                
                case 6:
                    respuesta = 0

        case 2:
            ruta = "lecciones/C/"
            ruta_practicas = "practicas/C/"
            match leccion:
                case 0:
                    respuesta = 2

                case 1:
                    respuesta = 3

                case 2:
                    respuesta = 1

                case 3:
                    respuesta = 1

                case 4:
                    respuesta = 1

                case 5:
                    respuesta = 0
                
                case 6:
                    respuesta = 3

                case 7:
                    respuesta = 0

                case 8:
                    respuesta = 3

    abrir_leccion = str(ruta) + "leccion_" + str(leccion+1) + ".txt" #Conjunta la ruta con el archivo correspondiente
    if lenguaje > 0: #Si es Python o C, Introducción es puro texto
        abrir_practica = str(ruta_practicas) + "practica_" + str(leccion+1) + ".txt"
        with open(abrir_practica, "r") as archivo_practica:
            texto_practica = archivo_practica.readlines()
            archivo_practica.close()
            posicion_inciso = len(texto_practica)-4 #posicion_inciso empieza en los últimos 4 lugares de la lista del texto de práctica
    
    with open(abrir_leccion, "r") as archivo_leccion:
        texto_leccion = archivo_leccion.readlines()
        archivo_leccion.close()

    linea = "____________________________________________________________________"
    posicion, tecla, posicion_pagina,  = 0, 0, False,  
    while True:
        os.system("cls")
        cuadro()
        print(f"{Cursor.POS(25, 3)}Bienvenido {nombre_usuario}")
        print(f"{Cursor.POS(24, 4)}{linea}")
        print(f"{Cursor.POS(25, 5)}{texto_leccion[0]}")
        y = 7
        if not posicion_pagina: #Si lección
            print(f"{Cursor.POS(83, 3)}Lección")
            for i in range(1, len(texto_leccion)):
                print(f"{Cursor.POS(25, y)}{texto_leccion[i]}")
                y += 1

        else: #Si práctica
            print(f"{Cursor.POS(83, 3)}Práctica")
            for i in range(len(texto_practica)-4): #Imprime la parte de arriba y la línea
                print(f"{Cursor.POS(25, y)}{texto_practica[i]}")
                y += 1

            for inciso in range(4): #Imprime los incisos
                if inciso == posicion: print(f"{Cursor.POS(25, y)}{Back.LIGHTCYAN_EX}{Fore.BLACK}{texto_practica[inciso+posicion_inciso]}")
                else: print(f"{Cursor.POS(25, y)}{texto_practica[inciso+posicion_inciso]}")
                y += 2

        tecla = ord(msvcrt.getch())
        match tecla:
            case 80: #Abajo
                if posicion_pagina:
                    posicion += 1
                    if posicion > 3: posicion = 0

            case 72: #Arriba
                if posicion_pagina:
                    posicion -= 1
                    if posicion < 0: posicion = 3

            case 75: #izquierda
                if posicion_pagina: posicion_pagina = False
                else: posicion_pagina = True

            case 77: #Derecha
                if posicion_pagina: posicion_pagina = False
                else: posicion_pagina = True
            
            case 13: #Enter
                if posicion_pagina: #Si andas en la práctica
                    if posicion == respuesta: #Si contestaste bien
                        print(f"{Cursor.POS(70, 25)}RESPUESTA CORRECTA")
                        print(f"{Cursor.POS(65, 26)}HAZ COMPLETADO LA LECCIÓN {leccion+1}")
                        if datos_json["cuentas"][id]["lecciones"][lenguaje] < leccion+1: #Si no habías completado la práctica, actualiza el json para marcarla
                            datos_json["cuentas"][id]["lecciones"][lenguaje] += 1
                            with open("cuentas.json", "w") as reemplazo:
                                json.dump(datos_json, reemplazo, indent=4)
                                reemplazo.close()

                        time.sleep(2)
                        return 0
                    
                    else:
                        print(f"{Cursor.POS(70, 25)}RESPUESTA INCORRECTA")
                        time.sleep(2)

                elif not lenguaje:
                    os.system("cls")
                    cuadro()
                    print(f"{Cursor.POS(45, 10)}HAZ COMPLETADO LA LECCIÓN {leccion+1}")
                    if datos_json["cuentas"][id]["lecciones"][lenguaje] < leccion+1:
                        datos_json["cuentas"][id]["lecciones"][lenguaje] += 1
                        with open("cuentas.json", "w") as reemplazo:
                            json.dump(datos_json, reemplazo, indent=4)
                            reemplazo.close()

                    time.sleep(2)
                    return 0

def menu_lecciones(lenguaje, id):
    with open("cuentas.json", "r") as datos:
        datos_json = json.load(datos)
        nombre_usuario = datos_json["cuentas"][id]["nombre"]
        c_lecciones = datos_json["lecciones"][lenguaje]
        datos.close()

    menu = []
    for i in range(c_lecciones):
        texto = "Lección " + str(i+1)
        menu.append(texto)

    menu.append("Salir")
    posicion, tecla = 0, 0
    linea = "____________________________________________________________________"
    while True:
        os.system("cls")
        cuadro()
        print(f"{Cursor.POS(25, 3)}Bienvenido {nombre_usuario}")
        print(f"{Cursor.POS(24, 4)}{linea}")
        print(f"{Cursor.POS(45, 6)}SELECCIONA UNA LECCIÓN")
        y = 7
        for i in range(len(menu)):
            if posicion == i: print(f"{Cursor.POS(25, y)}{Back.LIGHTCYAN_EX}{Fore.BLACK}{menu[i]}")
            else: print(f"{Cursor.POS(25, y)}{menu[i]}")
            y+=2
        
        tecla = ord(msvcrt.getch())
        match tecla:
            case 80:
                posicion += 1
                if posicion > len(menu)-1: posicion = 0

            case 72:
                posicion -= 1
                if posicion < 0: posicion = len(menu)-1

            case 13:
                if posicion == len(menu)-1:
                    return 0
                if posicion < datos_json["cuentas"][id]["lecciones"][lenguaje]+1:
                    ver_leccion(lenguaje, posicion, id)

                else:
                    print(f"{Cursor.POS(25, y)}Debes completar las lecciones anteriores")

def menu_lenguajes(id):
    with open("cuentas.json", "r") as datos:
        datos_json = json.load(datos)
        nombre_usuario = datos_json["cuentas"][id]["nombre"]
        datos.close()

    menu = ["Introducción a los lenguajes","Python", "C", "Salir"]
    linea = "____________________________________________________________________"
    posicion, tecla = 0, 0
    while True:
        os.system("cls")
        cuadro()
        print(f"{Cursor.POS(25, 3)}Bienvenido {nombre_usuario}")
        print(f"{Cursor.POS(24, 4)}{linea}")
        print(f"{Cursor.POS(45, 6)}SELECCIONA UN LENGUAJE");
        y = 9
        for i in range(len(menu)):
            if posicion == i: print(f"{Cursor.POS(25, y)}{Back.LIGHTCYAN_EX}{Fore.BLACK}{menu[i]}")
            else: print(f"{Cursor.POS(25, y)}{menu[i]}")
            if i < len(menu)-1: print(f"{Cursor.POS(70, y)}Progreso: {datos_json['cuentas'][id]['lecciones'][i]}%")
            y += 4

        tecla = ord(msvcrt.getch())
        match tecla:
            case 80:
                posicion += 1
                if posicion > len(menu)-1: posicion = 0

            case 72:
                posicion -= 1
                if posicion < 0: posicion = len(menu)-1

            case 13:
                if posicion == len(menu)-1:
                    return 0
                
                menu_lecciones(posicion, id)

def logup():
    menu = ["Nombre", "Ingresa correo", "Ingresa una contraseña", "Confirma tu contraseña", "Continuar", "Regresar"]
    nombre = " "
    correo = " "
    contra = " "
    confirmar_contra = " "
    posicion, tecla = 0, 0
    while True:
        os.system("cls")
        cuadro()
        y = 5
        for i in range(len(menu)):
            if posicion == i: print(f"{Cursor.POS(25, y)}{Back.LIGHTCYAN_EX}{Fore.BLACK}{menu[i]}")
            else: print(f"{Cursor.POS(25, y)}{menu[i]}")
            y += 4

        print(f"{Cursor.POS(52, 4)}CREA UNA CUENTA")
        print(f"{Cursor.POS(25, 7)}{nombre}")
        print(f"{Cursor.POS(25, 11)}{correo}")
        print(f"{Cursor.POS(25, 15)}{contra}")
        print(f"{Cursor.POS(25, 19)}{confirmar_contra}")
        tecla = ord(msvcrt.getch())
        match tecla:
            case 80:
                posicion += 1
                if posicion > len(menu)-1: posicion = 0

            case 72:
                posicion -= 1
                if posicion < 0: posicion = len(menu)-1

            case 13:
                match posicion:
                    case 0:
                        print(f"{Cursor.POS(25, 7)}                      ")
                        nombre = str(input(f"{Cursor.POS(25, 7)}"))

                    case 1:
                        print(f"{Cursor.POS(25, 11)}                      ")
                        correo = str(input(f"{Cursor.POS(25, 11)}"))

                    case 2:
                        print(f"{Cursor.POS(25, 15)}                      ")
                        contra = str(input(f"{Cursor.POS(25, 15)}"))

                    case 3:
                        print(f"{Cursor.POS(25, 19)}                      ")
                        confirmar_contra = str(input(f"{Cursor.POS(25, 19)}"))
                    
                    case 4:
                        if nombre != " " and correo != " " and contra != " " and confirmar_contra != " ":
                            if contra == confirmar_contra:
                                datos = {"nombre": nombre, "correo": correo, "contra": contra, "lecciones": [0, 0, 0]}
                                with open("cuentas.json", "r") as file:
                                    datos_json = json.load(file)
                                    ubicacion = datos_json["cuentas"]
                                    ubicacion.append(datos)
                                    file.close()
                                
                                with open("cuentas.json", "w") as nuevo:
                                    json.dump(datos_json, nuevo, indent=4)
                                    nuevo.close()
                                
                                return 0;
                    
                            else:
                                print(f"{Cursor.POS(27, 23)}Las contraseñas no coinciden")
                                time.sleep(2)

                        else:
                            print(f"{Cursor.POS(27, 23)}Por favor rellena los campos")
                            time.sleep(2)

                    case 5:
                        return 0

def login():
    try:
        with open("cuentas.json", "r") as archivo:
            cuentas = json.load(archivo)
            archivo.close()

    except:
        with open("cuentas.json", "w") as archivo:
            cuentas = {"cuentas": [], "lecciones":[2, 6, 8]}
            json.dump(cuentas, archivo, indent=4)
            archivo.close()
            login()

    correo = " "
    contra = " "
    posicion, tecla = 0, 0
    menu = ["Correo", "Contraseña", "Iniciar sesión", "Crear una cuenta"]
    while True:
        os.system("cls")
        cuadro()
        y = 5
        for i in range(len(menu)):
            if posicion == i: print(f"{Cursor.POS(25, y)}{Back.LIGHTCYAN_EX}{Fore.BLACK}{menu[i]}")
            else: print(f"{Cursor.POS(25, y)}{menu[i]}")
            y += 4

        print(f"{Cursor.POS(52, 4)}BIENVENIDO")
        print(f"{Cursor.POS(25, 7)}{correo}")
        print(f"{Cursor.POS(25, 11)}{contra}")
        tecla = ord(msvcrt.getch())
        match tecla:
            case 80:
                posicion += 1
                if posicion > len(menu)-1: posicion = 0

            case 72:
                posicion -= 1
                if posicion < 0: posicion = len(menu)-1

            case 13:
                match posicion:
                    case 0:
                        print(f"{Cursor.POS(25, 7)}                      ")
                        correo = str(input(f"{Cursor.POS(25, 7)}"))

                    case 1:
                        print(f"{Cursor.POS(25, 11)}                      ")
                        contra = str(input(f"{Cursor.POS(25, 11)}"))

                    case 2:
                        with open("cuentas.json", "r") as verificar:
                            datos_json = json.load(verificar)
                            for i in range(len(datos_json["cuentas"])):
                                if correo == datos_json["cuentas"][i]["correo"] and contra == datos_json["cuentas"][i]["contra"]:
                                    menu_lenguajes(i)
                                    correo = " "
                                    contra = " "
                                    posicion = 0
                                    break
                                
                                elif correo != datos_json["cuentas"][i]["correo"] or contra != datos_json["cuentas"][i]["contra"]:
                                    print(f"{Cursor.POS(42, y)}Comprueba los datos ingresados")
                                    time.sleep(2)
                                    break

                    case 3:
                        logup()

def main():
    init(autoreset=True)
    login()
main()