from colorama import init, Fore, Back, Cursor
import msvcrt
import json
import os
import time

def cuadro():
    linea = "_________________________________________________________________"
    y = 3
    print(f"{Cursor.POS(25, 2)}{linea}")
    for i in range(25):
        print(f"{Cursor.POS(24, y)}|{Cursor.POS(90, y)}|")
        y += 1

    print(f"{Cursor.POS(25, y-1)}{linea}")

def menu_lenguajes():
    return 0

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
            if posicion == i: print(f"{Cursor.POS(27, y)}{Back.LIGHTCYAN_EX}{Fore.BLACK}{menu[i]}")
            else: print(f"{Cursor.POS(27, y)}{menu[i]}")
            y += 4

        print(f"{Cursor.POS(52, 4)}CREA UNA CUENTA")
        print(f"{Cursor.POS(27, 7)}{nombre}")
        print(f"{Cursor.POS(27, 11)}{correo}")
        print(f"{Cursor.POS(27, 15)}{contra}")
        print(f"{Cursor.POS(27, 19)}{confirmar_contra}")
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
                        print(f"{Cursor.POS(27, 7)}                      ")
                        nombre = str(input(f"{Cursor.POS(27, 7)}"))

                    case 1:
                        print(f"{Cursor.POS(27, 11)}                      ")
                        correo = str(input(f"{Cursor.POS(27, 11)}"))

                    case 2:
                        print(f"{Cursor.POS(27, 15)}                      ")
                        contra = str(input(f"{Cursor.POS(27, 15)}"))

                    case 3:
                        print(f"{Cursor.POS(27, 19)}                      ")
                        confirmar_contra = str(input(f"{Cursor.POS(27, 19)}"))
                    
                    case 4:
                        if nombre != " " and correo != " " and contra != " " and confirmar_contra != " ":
                            if contra == confirmar_contra:
                                datos = {"nombre": nombre, "correo": correo, "contra": contra}
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

    except:
        with open("cuentas.json", "w") as archivo:
            cuentas = {"cuentas": [], "lecciones":[]}
            json.dump(cuentas, archivo, indent=4)
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
            if posicion == i: print(f"{Cursor.POS(27, y)}{Back.LIGHTCYAN_EX}{Fore.BLACK}{menu[i]}")
            else: print(f"{Cursor.POS(27, y)}{menu[i]}")
            y += 4

        print(f"{Cursor.POS(52, 4)}BIENVENIDO")
        print(f"{Cursor.POS(27, 7)}{correo}")
        print(f"{Cursor.POS(27, 11)}{contra}")
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
                        print(f"{Cursor.POS(27, 7)}                      ")
                        correo = str(input(f"{Cursor.POS(27, 7)}"))

                    case 1:
                        print(f"{Cursor.POS(27, 11)}                      ")
                        contra = str(input(f"{Cursor.POS(27, 11)}"))

                    case 2:
                        0

                    case 3:
                        logup()

def main():
    init(autoreset=True)
    login()

main()