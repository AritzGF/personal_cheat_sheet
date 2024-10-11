# Dockker

## Docker basico
```
docker info
```
```
docker version
```
**Crear contenedor**
```
docker run -d -p 5000:80 --name web nginxdemos/hello
```
- -d *Modo Demon*
- -p *Puertos*
- --name *Nombre del contenedor*

**Muestra contenedores**
```
docker ps
```
- -a *Muestra todos no solo los activos*
- -q *Solo muestra la IP*
- --filter *aplica filtro*
```
docker stop `Nombre-contenedor`
```
```
docker start `Nombre-contenedor`
```
```
docker restart `Nombre-contenedor`
```
**Borra contenedores**
```
docker rm
```
- -f *Fuerza a borrar el contenedor*
- -V *Borra los contenedores asignados*

**Borra todos los contenedores**
```
docker rm -f $(docker ps -aq)
```
**Copia del contenedor "web" /etc/hostname a la ubicacion actual "."**
```
docker cp web:/etc/hostname .
```
**Copia fichero.txt al contenedor web en la carpeta /tmp**
```
docker cp fichero.txt web:/tmp
```
**Exec ejecuta comandos en el contenedor indicado**
```
docker exec `Nombre-contenedor` `Comando-para-ejecutar`
```
- -i *Mantiene la entrada abierta*
- -t *Asigna un pseudo-terminal (tty), lo que hace que la salida sea más legible y te permite usar características interactivas del shell. (Gaby tiene que explicarlo)*
- -d *ejecuta en segundo plano*

**Abre una Shell en el contenedor**
```
docker exec -it `Nombre_contenedor` /bin/sh
```
---
## COMPOSE
### Nombre del archivo "docker-compose.yml*

**Crea el compose**
```
docker compose up
```
- -d *Los ejecuta en segundo plano*
- --build *Fuerza a recostruir los contenedores*

**Descarga las imagenes del compos**
```
docker compose pull
```
**Crea las imagenes definidas**
```
docker compose build
```
**Sube al servidor definido en el archivo docker-compose.yml**
```
docker compose push
```
**Borra los Contenedores creados con compose**
```
docker compose rm
```
**Borra todos los contenedores redes y volumenes creados con compose**
```
docker compose down
```
### Ejemplo docker-compose.yml
```
#Definimos contenedores
services:
#Nombre del contenedor
	bd:
#Imagen que vamos a usar
		image: mariadb:11.4
#Configuraciones de la imagen
		environment:
			- MYSQL_ROOT_PASSWORD=12345Abcde
			- MYSQL_DATABASE=egibide
			- MYSQL_USER=egibide
			- MYSQL_PASSWORD=12345Abcde
#Mapeo de los volumenes si va a usar
		volumes:
#Nombre_del_volumen:Punto_de_montado
			- mariadb:/var/lib/mysql
		expose:
			- 3306
	web:
		image: php:8.3-apache
#Si depende de otro contenedor
		depends_on:
			- bd
#Volumenlocal
		volumes:
#Ruta_local:Punto_de_Montado
			- ./www:/var/www/html
#Definimos puertos
		ports:
			- "80:80"
#Definimos volumenes
volumes:
#Nombre del volumen
	mariadb:
```
---
## Docker Build
### El nombre del archivo tiene que ser "Dockerfile"
**Crea la iso**
```
docker build . --tag `Nombre-Imagen`
```
**Poner etiquetas para subirlas a dockerhub**
```
docker tag `Nombre_ISO` `Nombre-Usuario/Nombre-ISO:etiqueta`
```
### Ejemplo Dockerfile
```
#Definir imagen base
FROM debian:latest 
#RUN corre comandos en el contenedor
RUN apt-get update -y
RUN apt-get install -y python3-pyfiglet
#Copia algo en el contenedor en este caso copia todo lo que ahi en nuetro directorioa a /app del contenedor
COPY . /app
#Define la ruta de trabajo
WORKDIR /app
#Ejecuta algo tiene prioridad a CMD
ENTRYPOINT ["python3"]
#Ejecuta algo 
CMD ["app.py"]
```
---
