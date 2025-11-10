# Gestor de Talleres (Flask)

Aplicación web desarrollada con **Flask** y **SQLAlchemy** para la gestión de talleres, alumnos e inscripciones.  
Forma parte del **entrega final de la materia Desarrollo y diseño de software Orientada a Objetos**, implementando un CRUD completo, ORM y buenas prácticas de arquitectura en Python.

---

## 📚 Descripción

El sistema permite:
- Crear, listar, editar y eliminar talleres.
- Registrar alumnos e inscribirlos en talleres.
- Usar **Blueprints** para modularizar controladores.
- Conectar a **SQLite** (modo desarrollo) o **MariaDB/MySQL** (modo producción).
- Implementar ORM con SQLAlchemy y queries parametrizadas.
- Reutilizar un mismo modal en HTML para crear y editar talleres desde la interfaz.

---

## ⚙️ Requisitos

- **Python 3.10+**
- **pip**
- **MariaDB** o **SQLite**
- Entorno virtual `venv`

### Dependencias principales
(Están listadas en `requirements.txt`)
- `Flask`
- `Flask-SQLAlchemy`
- `pymysql` o `mariadb-connector-python` (según motor)

---

## 🧩 Estructura del proyecto
```
    /project-root
    ├─ app.py # punto de entrada principal
    ├─ config/
    │ └─ database.py # configuración de la base de datos
    ├─ controllers/ # endpoints y blueprints
    ├─ domain/ # entidades (Taller, Alumno, Inscripcion)
    ├─ exceptions/ # manejo de errores personalizados
    ├─ repositories/ # capa de acceso a datos
    ├─ services/ # lógica de negocio
    ├─ static/
    │ └─ css/
    ├─ templates/ # vistas HTML con Jinja2
    ├─ .venv/ # entorno virtual
    └─ requirements.txt

```
---

## 💻 Instalación y ejecución

Los pasos asumen que estás ubicado en la **raíz del proyecto** (`src` o `project-root`).

###  Crear y activar entorno virtual

**Windows (PowerShell):**
```powershell
    py -3 -m venv .venv 
```
```powershell
    venv\Scripts\activate
```

Al activarlo, verás (.venv) al inicio de la línea en la terminal.

### Instalar dependencias

```powershell
    pip install -r requirements.txt
```
Si no existe el archivo, podés instalar manualmente:

```powershell
    pip install flask flask-sqlalchemy
    pip install pymysql        # si usas MariaDB/MySQL
```
###  Ejecutar la aplicación (modo debug)
Opción A – usando Flask:

```powershell
    flask --app app --debug run
```

## 🌐 Rutas principales
| Método | Ruta                      | Descripción     |
| ------ | ------------------------- | --------------- |
| `GET`  | `/talleres/`              | Listar talleres |
| `POST` | `/talleres/crear`         | Crear taller    |
| `POST` | `/talleres/editar/<id>`   | Editar taller   |
| `POST` | `/talleres/eliminar/<id>` | Eliminar taller |

url_for('talleres.listar_talleres') usa el formato blueprint_name.funcion, lo que evita problemas si el prefijo cambia.




## 🧠 Detalles del front-end
- Las vistas están en la carpeta templates/.
- El modal es reutilizable: sirve tanto para crear como para editar talleres.
- En el JavaScript:

    - Se cambia dinámicamente el título (Nuevo Taller / Editar Taller).

    - Se modifica la acción del formulario (/talleres/crear o /talleres/editar/<id>).

    - Los campos se rellenan usando los data-* atributos de cada botón editar.

- Se usa method="POST" para crear y editar, porque los formularios HTML no soportan PUT ni DELETE nativos.



### Abrí en el navegador:
👉 http://127.0.0.1:5000

### 👥 Integrantes
- Juan Carlos Vilcherrez 
- Diego
- Gaston
- Cesar