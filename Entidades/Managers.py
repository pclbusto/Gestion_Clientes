from Entidades.Entity_Manager import Entity_Manager
from Entidades import Init
from Entidades.Entidades_Paquete import *


class Clientes(Entity_Manager):

    def __init__(self, session=None):
        Entity_Manager.__init__(self, session=session, clase=Cliente)
        if session is not None:
            self.session = session
        else:
            self.session = Init.Session()

        self.lista_opciones = {'Id': Cliente.id, 'apellido': Cliente.apellido}

        self.status = 1
        self.entidad = Cliente()
        self.set_order(Cliente.apellido, 0)
        self.filtro = None
        self.direccion = 0

    def save(self):
    #     verificamos que no existe ese cliente buscando por numero de documento
        pass
    def rm(self, id):
        Entity_Manager.rm(self)
        self.session.query(Cliente).filter(Cliente.id == id).delete()
        self.session.commit()

if (__name__ == '__main__'):
    clientes_mng = Clientes()
    cliente = clientes_mng.new_record()
    cliente.nombre = "Pedro"
    cliente.apellido = "Busto"
    cliente.numero_telefono="2664649791"
    clientes_mng.save()
