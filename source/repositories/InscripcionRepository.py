from sqlalchemy import create_engine, text

sqlite_engine = create_engine("mariadb+mariadbconnector://root:root@127.0.0.1:3306/gestor-dsoo")

class InscripcionRepository:
    def obtener_todas(self):
        with sqlite_engine.connect() as con:
            query = text("""
                SELECT i.id, a.nombre AS alumno_nombre, a.apellido AS alumno_apellido,
                       t.nombre AS taller_nombre, t.modalidad
                FROM inscripciones i
                JOIN alumnos a ON i.id_alumno = a.id
                JOIN talleres t ON i.id_taller = t.id
            """)
            result = con.execute(query)
            return result.fetchall()

    def crear(self, data):
        with sqlite_engine.begin() as con:  
            query_taller = text("SELECT cupos_disponibles FROM talleres WHERE id = :id_taller")
            taller = con.execute(query_taller, {"id_taller": data["id_taller"]}).fetchone()

            if not taller or taller.cupos_disponibles <= 0:
                raise ValueError("No hay cupos disponibles")

            query_insert = text("""
                INSERT INTO inscripciones(id_taller, id_alumno)
                VALUES (:id_taller, :id_alumno)
            """)
            con.execute(query_insert, data)

            query_update = text("""
                UPDATE talleres
                SET cupos_disponibles = cupos_disponibles - 1
                WHERE id = :id_taller
            """)
            con.execute(query_update, {"id_taller": data["id_taller"]})
