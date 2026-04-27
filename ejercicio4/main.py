"""
Módulo que crea un directorio y lo envía a la papelera usando send2trash.
"""
from send2trash import send2trash
import os

def crear_y_eliminar_directorio():
    """Crea un directorio test_dir y lo envía a la papelera.

    Returns:
        None
    """
    os.mkdir("test_dir")
    print("Directorio test_dir creado.")
    
    send2trash("test_dir")
    print("Directorio test_dir enviado a la papelera.")

crear_y_eliminar_directorio()