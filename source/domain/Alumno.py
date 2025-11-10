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
    