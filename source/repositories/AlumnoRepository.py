from sqlalchemy import create_engine, text

sqlite_engine = create_engine("mariadb+mariadbconnector://root:root@127.0.0.1:3306/gestor-dsoo")

class AlumnoRepository:
    def obtener_todos(self):
        with sqlite_engine.connect() as con:
            return con.execute(text("SELECT * FROM alumnos ORDER BY apellido, nombre")).fetchall()

    def obtener_por_id(self, id):
        with sqlite_engine.connect() as con:
            row = con.execute(text("SELECT * FROM alumnos WHERE id=:id"), {"id": id}).fetchone()
            if not row:
                raise Exception("Alumno no encontrado")
            return row

    def crear(self, data):
        with sqlite_engine.begin() as con:
            con.execute(
                text("INSERT INTO alumnos(dni, nombre, apellido) VALUES (:dni, :nombre, :apellido)"),
                data
            )
