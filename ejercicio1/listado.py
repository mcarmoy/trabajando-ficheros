"""
Módulo que muestra los archivos del directorio actual usando rich.
"""

import os
from rich.console import Console
from rich.panel import Panel

def listar_archivos():
    """
    Lista todos los archivos del directorio actual
    con formato visual usando rich.
    """
    console = Console()
    archivos = os.listdir(".")
    contenido = "\n".join(archivos)
    console.print(Panel(contenido, title="Archivos del directorio"))

listar_archivos()