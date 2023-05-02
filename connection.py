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
        '''
        Initializes database using sqlalchemy
        No params passed on this constructor
        Takes datas declared up
        '''
        self.engine = create_engine(connection_string, echo=True)
        self.Session = sessionmaker(bind=self.engine)
        self.session = self.Session()
        self.base = Base

    def dropTable(self):
        '''
        Drops all tables from database
        No parameters provides
        Void method
        '''
        self.base.metadata.drop_all(self.engine)

    # model methode for overriding
    def createTable():
        '''
        The method used for override
        '''
        print('create table')

    # model methode for overriding
    def initializeDatas():
        '''
        The method used for override
        '''
        print('initialize data')
