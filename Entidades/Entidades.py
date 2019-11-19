import Entidades
from sqlalchemy import Column, Integer, String

class Cliente(Entidades.Init.Base):
    '''Matiene los datos basicos de un cliente
    '''
    __tablename__='cliente'

    id = Column(Integer, primary_key=True)
    nombre = Column(String, nullable=False, default='')
    apellido = Column(String, nullable=False, default='')
    direccion = Column(String, nullable=False, default='')
    numero_telefono = Column(String, nullable=False, default='')

    def __repr__(self):
        return "id={}\nnombre={}Apellido={}\nApellido={}\nDireccion={}\nNumero Telefono={}\n".format(self.id, self.nombre, self.apellido.direccion, self.numero_telefono)
