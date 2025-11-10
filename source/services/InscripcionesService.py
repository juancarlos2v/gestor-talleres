from repositories.InscripcionRepository import InscripcionRepository

class InscripcionService:
    def __init__(self):
        self.repo = InscripcionRepository()

    def obtener_todas(self):
        return self.repo.obtener_todas()

    def obtener_talleres(self):
        return self.repo.obtener_talleres()

    def crear(self, data):
        dni = data.get("dni")
        id_taller = data.get("id_taller")

        if not dni or not id_taller:
            raise ValueError("Faltan datos obligatorios")

        # Buscar el alumno
        id_alumno = self.repo.obtener_alumno_por_dni(dni)
        if not id_alumno:
            raise ValueError("El alumno con ese DNI no existe")

        data["id_alumno"] = id_alumno
        self.repo.crear(data)
