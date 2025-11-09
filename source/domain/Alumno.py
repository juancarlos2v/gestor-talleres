from exceptions import DatosInvalidosError
from app import db

class Alumno(db.Model) :
    __tablename__ = 'alumnos'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50))
    apellido = db.Column(db.String(50))
    dni=db.Column(db.String(250))

    def __init__(self,dni,nombre,apellido):
        self.dni=dni
        self.nombre=nombre
        self.apellido=apellido

    @property
    def dni(self):
        return self.dni
    
    @property
    def nombre(self):
        return self.nombre
    
    @property
    def apellido(self):
        return self.apellido
    
    def validar(self):
        isValid=self.dni and self.nombre and self.apellido

        if not isValid:
            raise DatosInvalidosError("Todos los campos son obligatorios.")