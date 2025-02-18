# Compartir archivos

## Netcat
**Enviar**
```
cat archivo.txt | nc -lvp 4444
```
**Recibir**
```
nc 192.168.25.10 4444 > archivo.txt
```

## Pyhton HTTP
**Enviar**
```
python3 -m http.server 80
```
**Recibir(wget)**
```
wget http://192.168.25.10:80/archivo.txt
```
**Recibir(curl)**
```
curl 192.168.25.10:80/archivo.txt -o archivo.txt
```

## SSH
**Enviar**
```
scp archivo.txt user@192.168.25.100:/tmp
```

**Descargar**
```
scp user@192.168.25.100:/ruta/del/archivo.txt ./
```

## Socat
**Enviar**
```
./socat -u File:archivo.txt TCP:4444, reuseaddr
```
**Recibir**
```
./socat -u TCP:192.168.25.10:4444 STDOUT > archivo.txt
```

