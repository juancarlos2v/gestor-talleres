from domain.Taller import Taller
from repositories.TallerRepository import TallerRepository

class TallerService():

    def __init__(self):
        self.repo=TallerRepository()

    def crear_taller(self,nombre,modalidad,cupo,fecha):
        taller= Taller(nombre,modalidad,cupo,fecha)
        taller.validar()
        self.repo.save(taller)
        return taller
    
    def editar_taller(self, id, nombre, modalidad, cupo, fecha):
        self.repo.update(id, nombre, modalidad, cupo, fecha)

    
    def eliminar_taller(self,id):
        self.repo.delete(id)
    


