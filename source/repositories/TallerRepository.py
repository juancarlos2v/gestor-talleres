from domain.Taller import Taller,db

class TallerRepository:
    
    def get_all(self):
       return Taller.query.all()
    
    def save(sef,taller):
        db.session.add(taller)
        db.session.commit()

    def delete(self,id):
        taller=Taller.query.get(id)
        db.session.delete(taller)
        db.session.commit()

    def update(self, id, nombre, modalidad, cupo, fecha):
        taller = Taller.query.get(id)
        if taller:
            taller.nombre = nombre
            taller.modalidad = modalidad
            taller.cupo = cupo
            taller.fecha = fecha
            db.session.commit()
