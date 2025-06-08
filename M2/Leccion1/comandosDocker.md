## 🐳 **Comandos generales**

| Comando          | Descripción                                                             |
| ---------------- | ----------------------------------------------------------------------- |
| `docker version` | Muestra la versión del cliente y del servidor Docker.                   |
| `docker info`    | Muestra detalles del sistema Docker (contenedores, imágenes, red, etc). |
| `docker help`    | Muestra ayuda general o de un comando específico (`docker help run`).   |

---

## 📦 **Comandos de contenedores**

| Comando          | Descripción                                                                              |
| ---------------- | ---------------------------------------------------------------------------------------- |
| `docker run`     | Crea y ejecuta un nuevo contenedor desde una imagen. Ej: `docker run -it ubuntu bash`.   |
| `docker start`   | Inicia un contenedor detenido.                                                           |
| `docker stop`    | Detiene un contenedor en ejecución.                                                      |
| `docker restart` | Reinicia un contenedor.                                                                  |
| `docker pause`   | Pausa todos los procesos en un contenedor.                                               |
| `docker unpause` | Reanuda un contenedor pausado.                                                           |
| `docker kill`    | Mata el proceso principal de un contenedor.                                              |
| `docker rm`      | Elimina uno o varios contenedores detenidos.                                             |
| `docker ps`      | Lista contenedores en ejecución. Usa `-a` para ver todos (incluyendo detenidos).         |
| `docker exec`    | Ejecuta un comando en un contenedor en ejecución. Ej: `docker exec -it contenedor bash`. |
| `docker attach`  | Se conecta a un contenedor en ejecución (como si fuera una terminal).                    |
| `docker logs`    | Muestra los logs de salida de un contenedor.                                             |

---

## 🧱 **Comandos de imágenes**

| Comando         | Descripción                                                                     |
| --------------- | ------------------------------------------------------------------------------- |
| `docker pull`   | Descarga una imagen desde Docker Hub (o repositorio privado).                   |
| `docker build`  | Crea una imagen a partir de un `Dockerfile`. Ej: `docker build -t mi-imagen .`. |
| `docker push`   | Sube una imagen a un registro (como Docker Hub).                                |
| `docker images` | Lista las imágenes disponibles en tu máquina.                                   |
| `docker rmi`    | Elimina una o más imágenes.                                                     |
| `docker tag`    | Asigna una etiqueta (tag) a una imagen. Ej: `docker tag imgid repo:version`.    |
| `docker save`   | Guarda una imagen como archivo `.tar`.                                          |
| `docker load`   | Carga una imagen desde un archivo `.tar`.                                       |
| `docker import` | Crea una imagen desde un sistema de archivos `.tar`.                            |
| `docker export` | Exporta un contenedor como `.tar`, sin historial.                               |

---

## 🛠️ **Comandos de volúmenes**

| Comando                 | Descripción                            |
| ----------------------- | -------------------------------------- |
| `docker volume create`  | Crea un volumen persistente.           |
| `docker volume ls`      | Lista todos los volúmenes.             |
| `docker volume inspect` | Muestra detalles de un volumen.        |
| `docker volume rm`      | Elimina uno o varios volúmenes.        |
| `docker volume prune`   | Elimina todos los volúmenes no usados. |

---

## 🌐 **Comandos de red**

| Comando                     | Descripción                          |
| --------------------------- | ------------------------------------ |
| `docker network create`     | Crea una red para contenedores.      |
| `docker network ls`         | Lista las redes disponibles.         |
| `docker network inspect`    | Muestra detalles de una red.         |
| `docker network rm`         | Elimina una red.                     |
| `docker network connect`    | Conecta un contenedor a una red.     |
| `docker network disconnect` | Desconecta un contenedor de una red. |

---

## 🧹 **Comandos de limpieza**

| Comando                  | Descripción                                                                                               |
| ------------------------ | --------------------------------------------------------------------------------------------------------- |
| `docker system prune`    | Elimina todos los contenedores detenidos, redes no usadas, imágenes sin etiqueta y caché de construcción. |
| `docker container prune` | Elimina contenedores detenidos.                                                                           |
| `docker image prune`     | Elimina imágenes sin etiqueta (dangling).                                                                 |
| `docker volume prune`    | Elimina volúmenes sin usar.                                                                               |
| `docker builder prune`   | Limpia cachés de construcción (`build`).                                                                  |

---

## 🧪 **Comandos de inspección y debug**

| Comando          | Descripción                                                            |
| ---------------- | ---------------------------------------------------------------------- |
| `docker inspect` | Devuelve en JSON los detalles de un contenedor, volumen, red o imagen. |
| `docker stats`   | Muestra el uso de CPU, memoria y red en tiempo real por contenedor.    |
| `docker top`     | Muestra los procesos que corren dentro de un contenedor.               |
| `docker diff`    | Muestra los cambios hechos al sistema de archivos de un contenedor.    |
| `docker events`  | Muestra eventos en tiempo real del demonio de Docker.                  |

---

## 🧰 **Otros útiles**

| Comando          | Descripción                                                      |
| ---------------- | ---------------------------------------------------------------- |
| `docker login`   | Inicia sesión en Docker Hub o registro privado.                  |
| `docker logout`  | Cierra sesión del registro.                                      |
| `docker context` | Maneja múltiples entornos de Docker (local, remoto, cloud, etc). |

---
