from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
import config
'''
el argument connect args check_same_thread en false sirve para poder hacer consultas en threads
y que no de error despues al usuarlo poque no se creo en el mismo thread.
'''
pathdb = os.path.join(config.database_path, config.database_name)
# print(pathdb )
engine = create_engine('sqlite:///'+pathdb, echo=False, connect_args={'check_same_thread': False})
Base = declarative_base()
Session = sessionmaker(bind=engine)



def recreateTablesAll():
    Base.metadata.create_all(engine)
