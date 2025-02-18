# Chisel

**Crear servidor**
```
./chisel server --reverse -p 2525
```
Chisel escucha en el puerto 2525

**Crear cliente***
```
./chisel client 192.168.25.10:2525 R:socks
```
Se comunica con el servidor que le digamos en el puerto que le especifiquemos *127.0.0.1:2525*

**Crear cliente 2***
```
./chisel client 192.168.26.100:2525 R:2626:socks
```
"R:2626:socks" le indica en que puerto abrira el tunel si no ponemos puerto lo habre en el por defecto
