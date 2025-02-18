# SSH Pivoting

## Local Port Forwanding
Redirige trafico de la maquina local a una remota
```
ssh -L [puerto_local]:[destino_remoto]:[puerto_remoto] [usuario]@[servidor_ssh]
```
```
ssh -L 8080:localhost:80 usuario@192.168.25.100
```

## Remote Port Forwanding
Redirige trafico de la maquina remota a la maquina local
```
ssh -R [puerto_remoto]:[destino_local]:[puerto_local] [usuario]@[servidor_ssh]
```
```
ssh -R 8080:localhost:80 usuario@192.168.25.100
```

## Dynamic Port Forwanding(Proxy SOCKS)
Establece un servidor proxy
```
ssh -D [puerto_local] [usuario]@[servidor_ssh]
```
```
ssh -D 1080 usuario@192.168.25.100
```

## .ssh/config(Pivoting)
Configuracion para saltos automaticos con ssh
```
Host host1
    HostName 192.168.25.100
    User admin

Host host2
    HostName 192.168.26.101
    User admin
    ProxyJump host1

Host host3
    HostName 192.168.27.102
    User admin
    ProxyJump host2

Host host4
    HostName 192.168.28.103
    User admin
    ProxyJump host3


```
