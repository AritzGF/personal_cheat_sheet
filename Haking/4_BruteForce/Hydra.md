# HYDRA

**Ataque basico**

```
hydra -l usuario -p password servicio://IP -V
```

**Ataque con diccionario**
```
hydra -L lista_usuarios.txt -P lista_password.txt servicio://IP -V
```

**Ejemplo**
```
hydra -l admin -P rockyou.txt ssh://127.0.0.1 -V
```
|Comando|Funcion|
|:---:|---|
|-l|Usuario|
|-L|Lista de usuarios|
|-p|Contraseña|
|-P|Lista de contraseñas|
|-V|Muestra todos los intentes|
|-o|Guarda resultados en fichero especificado|
|-t|Liminta numeros de intentes simultaneos|
|-c|Limita el tiempo entre intentos|
