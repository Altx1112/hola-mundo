from colorama import init, Fore, Back, Cursor
import msvcrt
import json
import os

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
    return 0

def login():
    try:
        with open("cuentas.json", "r") as archivo:
            cuentas = json.load(archivo)

    except:
        with open("cuentas.json", "w") as archivo:
            cuentas = {"cuentas": []}
            json.dump(cuentas, archivo, indent=4)
            login()

    correo = " "
    contrasena = " "
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
        print(f"{Cursor.POS(27, 11)}{contrasena}")
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
                        contrasena = str(input(f"{Cursor.POS(27, 11)}"))

                    case 2:
                        0

                    case 3:
                        logup()

def main():
    init(autoreset=True)
    login()

main()