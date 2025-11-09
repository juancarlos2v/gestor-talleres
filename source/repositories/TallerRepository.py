from domain.Taller import Taller

class TallerRepository:
    
    def get_all(self):
       return Taller.query.all()