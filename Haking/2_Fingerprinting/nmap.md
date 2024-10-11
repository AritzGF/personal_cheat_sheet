# NMAP

**Escaneo rapido de puertos**
```
nmap `ip.obgetivo`
```
**Escaneo de puetos rango personalizado**
```
nmap -p `rango-personalizado` `ip.obgetivo`
```
```
nmap -p 20-22 192.168.1.25
```
**Escaneo de una red**
```
nmap -sn `ip.de.la.red/mascara`
```
**Escaneo de red mas puertos**
```
nmap -sN `ip.de.la.red/mascara`
```
**Escaneo de un equipo**
``` 
nmap -sS -A `ip.del.equipo`
```
