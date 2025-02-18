# Socat

**Reenvio de Puertos**
```
./socat TCP-LISTEN:2525,fork TCP:192.168.25.10:2626

```
```
./socat UDP-LISTEN:2525,fork UDP:192.168.25.10:2626

```
Todo lo que entre por el puerto "2525" lo redirige a la maquina "127.0.0.1:2626"
