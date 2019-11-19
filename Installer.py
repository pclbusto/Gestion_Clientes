import os
from Entidades import Init
import Entidades.Entidades_Paquete

if __name__ == '__main__':
    session = Init.Session()
    Init.recreateTablesAll()
