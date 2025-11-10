from app import db

class Inscripcion(db.Model) :
    __tablename__ = 'alumnos'
    id = db.Column(db.Integer, primary_key=True)
    id_taller = db.Column(db.Integer(11))
    id_taller=db.Column(db.Integer(11))

    def __init__(self,id_alumno,id_taller):
        self.id_taller=id_alumno
        self.id_taller=id_taller
    