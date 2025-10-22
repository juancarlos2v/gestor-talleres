from exceptions import DatosInvalidosError

class Talleres:
    def __init__(self,nombre,modalidad,cupo,fecha):
        self.nombre=nombre
        self.modalidad=modalidad
        self.cupo=cupo
        self.fecha=fecha
    
    @property
    def nombre(self):
        return self.nombre
    
    @property
    def modalidad(self):
        return self.modalidad
    
    @property
    def cupo(self):
        return self.modalidad
    
    @property
    def fecha(self):
        return self.fecha
    
    def validar(self):
        isValid=self.dni and self.nombre and self.apellido

        if not isValid:
            raise DatosInvalidosError("Todos los campos son obligatorios.")