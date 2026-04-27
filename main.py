"""
Módulo que muestra el nombre y ruta absoluta de cada archivo del directorio actual.
"""
from pathlib2 import Path

def mostrar_rutas():
    """Muestra el nombre y ruta absoluta de cada archivo del directorio actual.

    Returns:
        None
    """
    ruta_actual = Path(".")
    for archivo in ruta_actual.iterdir():
        if archivo.is_file():
            print(f"Nombre: {archivo.name}")
            print(f"Ruta absoluta: {archivo.resolve()}")
            print("---")

mostrar_rutas()