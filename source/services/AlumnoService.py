from domain.Alumno import Alumno
from exceptions.DatosInvalidosError import DatosInvalidosError
from repositories.AlumnoRepository import AlumnoRepository

class AlumnoService():
    def __init__(self):
        self.repo = AlumnoRepository()

    def obtener_todos(self):
        return self.repo.obtener_todos()

    def obtener_por_id(self, id):
        return self.repo.obtener_por_id(id)

    def crear(self, data):
        print(data.get('dni'))
        # Validaciones
        if not data.get('dni') or not data.get('nombre') or not data.get('apellido'):
            raise DatosInvalidosError("DNI, nombre y apellido son obligatorios")
        self.repo.crear(data)
        # try:
        #     self.repo.crear(data)
        # except Exception:
        #     raise DniDuplicadoError("Ya existe un alumno con ese DNI")