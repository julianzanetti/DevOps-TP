# TP10-DevOps
# Integrantes

- Julian Zanetti
- Eduardo Ghidoli
- Ricardo Pacheco
- Franco Lizarraga


Para este Proyecto utilizamos de base el tp6 que levanta una pagina web de administracion de personas creada con Pyhton-Django y incluye un motor de base de datos Postgresql.

## Paso 0: Instalar Herramientas/Entorno de trabajo

1. En este repositorio verán un directorio llamado Parte 1 que contiene el vagrant file, el cual nos permitira levantar una maquina virtual con las herramientas necesarias para el proyecto (docker, minikube, kubectl, argocd cli, jenkins, etc)

Para poder levantar esta maquina, iremos al directorio Vagrant y corremos el siguiente comando:

```
vagrant up
```

1. Ya con la maquina virtual levantada, nos podremos conectar con el siguiente comando

```
vagrant ssh
```

1. ahora levantamos el servicio de Jenkins 
- Asegúrate de tener el plugin "Docker Pipeline" instalado en tu instancia de Jenkins.
- Crea un nuevo trabajo en Jenkins y elige "Pipeline" como tipo de trabajo.
- En la configuración del trabajo, elige "Pipeline script from SCM" como la definición del script y selecciona tu sistema de control de versiones (Git, por ejemplo).
- Especifica la URL del repositorio y el nombre del script (Jenkinsfile) que se encuentra en el directorio parte 3.

---

## Paso 1: Dockerfile

1. Para construir la imagen de docker podremos hacerlo de forma manual descargando el codigo y haciendo un docker build del directorio Parte 2 

---

## Paso 2: Kubernetes

1. Para este paso es tan simple como verificar estar conectados a nuestro cluster de kubernetes (poder ejecutar un kubectl get pods -A sin errores) y asi crear nuestros recursos dentro del directorio Kubernetes con el siguiente comando:

```
kubectl apply -f Kubernetes/kubectl.yaml
```

El contenido del yaml se encuentra en el directorio parte 4

---

## Paso 3: ArgoCD y Helm

### 1* **Desplegar Argo CD**

```bash

minikube start
argocd repo add nombre_repo
kubectl create ns testing (Creamos el Namespace "testing" que será el que usaremos para desplegar la aplicacion)

```

### 2* **Acceder a la interfaz de usuario de Argo CD**

```bash

kubectl port-forward svc/argocd-server -n argocd 8080:443
```

Ahora, accede a la interfaz de usuario de Argo CD abriendo http://localhost:8080 en el navegador. Inicia sesión con el nombre de usuario predeterminado (**`admin`**) y la contraseña obtenida con el siguiente comando:

```bash
kubectl -n argocd get secret argocd-initial-admin-secret -o jsonpath="{.data.password}" | base64 -d (Obtenemos la pass de argo)
```

### 3* **Desplegar una Aplicación**

Creamos la definición de aplicación que se encuentra en el yaml “kubectl.yaml” en el directorio parte 5

### **4* Sincronizar la Aplicación**

Visita la interfaz de usuario de Argo CD, busca la aplicación que levantamos y haz clic en el botón "Sync" para implementar tu aplicación.

---

### Paso 4: Convertir a Helm

Para esto vamos a usar la aplicación de Windows **[Helmify](https://github.com/arttor/helmify/releases/download/v0.4.10/helmify_Windows_x86_64.zip)**

1* una vez descargada descomprimimos y ejecutamos un powershell como administrador 

2* Copiamos el Yaml de la parte 5 /Helm en la misma ruta de donde descomprimimos la aplicacion

3* navegamos en powershell hasta la ruta de la aplicacion helmify y usamos el sig comando para convertir nuestro yaml

```jsx
helmify -f /my_directory -r kubectl.yaml
```

esto nos creara 1 carpeta y 2 archivos, denstro de la carpeta templates estara el archivo convertido

En la interfaz de argo si levantamos el Helm nos deberia dar todo OK

![helm 2](https://github.com/francoolizarraga/TP10-DevOps/assets/116183200/ca4e1909-ee5f-4569-9031-ed60be3884b6)




Deploy de ambas metodologias corriendo

![helm](https://github.com/francoolizarraga/TP10-DevOps/assets/116183200/2f0065f4-837f-48f4-b0be-a8ab88538928)






