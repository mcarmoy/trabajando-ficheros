"""
Módulo que recorre el directorio actual e imprime
archivos en verde y carpetas en azul usando colorama.
"""

import os
from colorama import init, Fore

init()

def inspector_tipos():
    """
    Recorre el directorio actual e imprime cada elemento
    en verde si es archivo o en azul si es carpeta.
    """
    elementos = os.listdir(".")
    
    for elemento in elementos:
        if os.path.isfile(elemento):
            print(Fore.GREEN + elemento)
        else:
            print(Fore.BLUE + elemento)

inspector_tipos()