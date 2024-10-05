# GIT
	
## Git basico
**Definir nombre del que manipula el proyecto**
```
git config --global user.name `Nombre Apellidos`
```
**Define correo del que manipula el correo**
```
git config --global user.email `nobody@ikasle.egibide.org`
```
**Ves la configuracion global**
```
git config --global --list 
```
**Muestra estado**
```
git status 
```
**historial de commits**
```
git log 
```
---
## Crear proyecto

**Inicia el proyecto**
```
git init `Nombre-Proyecto`
```
**Añade archivo para el commit**
```
git add `archibo-con-cambios` 
```
**Crea el commit**
```
git commit -m `Nombre-commit` 
```
---
## Repo en la nube
**copias el git de un repo**
```
git clone `URL-del-repo`
```
**Subir cambios al servidor**
```
git push
```
**vincula repo local con repo en la nube**
```
git remote add `rama(normalmete "main" o "origin")" "URL-del-repo` 
```
**Primer push**
```
git push -u origin master 
```
---
## Ramificar
**Crea una rama**
```
git branch `Nombre-rama`
```
**Moverte entre ramas** 
```
git switch `Nombre-rama`
```
**Fusiona rama actual con rama mencionada**
```
git merge `Nombre-rama` 
```
---
