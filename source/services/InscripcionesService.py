from repositories.InscripcionRepository import InscripcionRepository

class InscripcionService:
    def __init__(self):
        self.repo = InscripcionRepository()

    def obtener_todas(self):
        return self.repo.obtener_todas()

    def crear(self, data):
        # Validaciones básicas
        if not data.get('id_taller') or not data.get('id_alumno'):
            raise ValueError("Taller y alumno son obligatorios")

        self.repo.crear(data)