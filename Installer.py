import os
from Entidades import Init
import Entidades.Entidades

if __name__ == '__main__':
    session = Init.Session()
    Init.recreateTablesAll()
