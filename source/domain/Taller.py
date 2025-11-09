from exceptions import DatosInvalidosError
from config.database import db

class Taller(db.Model):

    __tablename__ = 'talleres'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    modalidad = db.Column(db.String(100), nullable=False)
    cupo = db.Column(db.Integer, nullable=False)
    fecha = db.Column(db.Date, nullable=False)


    def __init__(self,nombre,modalidad,cupo,fecha):
        self.nombre=nombre
        self.modalidad=modalidad
        self.cupo=cupo
        self.fecha=fecha
    
    def validar(self):
        isValid=self.nombre and self.modalidad and self.cupo

        if not isValid:
            raise DatosInvalidosError("Todos los campos son obligatorios.")