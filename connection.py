from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import os
from sqlalchemy.orm import declarative_base


BASE_DIR = os.path.dirname(os.path.realpath(__file__))
connection_string = "sqlite:///" + \
    os.path.join(BASE_DIR, 'database', 'python_assignment.db')
Base = declarative_base()


class Connection:
    def __init__(self):
        self.engine = create_engine(connection_string, echo=True)
        self.Session = sessionmaker(bind=self.engine)
        self.session = self.Session()
        self.base = Base

    def dropTable(self):
        self.base.metadata.drop_all(self.engine)

    # model methode for overriding
    def createTable():
        print('create table')

    # model methode for overriding
    def initializeData():
        print('initialize data')
