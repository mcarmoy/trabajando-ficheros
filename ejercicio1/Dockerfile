# Imagen base de Python
FROM python:3.11-slim

# Carpeta de trabajo dentro del contenedor
WORKDIR /app

# Copiamos primero el requirements para aprovechar caché
COPY requirements.txt .

# Instalamos las librerías
RUN pip install -r requirements.txt

# Copiamos el resto del código
COPY . .

# Comando que se ejecuta al arrancar el contenedor
CMD ["python3", "listado.py"]