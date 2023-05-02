import sys
from connection import Connection
import pandas as pd
import unittest


class IdealData(Connection):
    def __init__(self):
        '''
        Constructor of this class
        It initialises base class Connection
        '''
        super().__init__()

    def createTable(self):
        '''Create table method overided from Connection'''
        self.base.metadata.create_all(self.engine)

    def initializeDatas(self):
        '''
        Initializes ideal datas on ideal_data table
        It replaces them if it exists
        No params needed
        Void method
        Reads data from the file ideal.csv under dataset folder
        '''
        try:
            df = pd.read_csv('dataset/ideal.csv')
            self.createTable()
            df.to_sql('ideal_data', self.engine,
                      if_exists='replace', index=False)
        except:
            exception_type, exception_value, exception_traceback = sys.exc_info()
            print("Exception Type: {}\nException Value: {}".format(exception_type,
                                                                   exception_value))

    def loadDatas(self):
        '''
        Used to load datas from database
        No params provided
        Returns all rows from ideal_data table
        '''
        try:
            return pd.read_sql_table(
                'ideal_data', self.engine.connect())
        except:
            exception_type, exception_value, exception_traceback = sys.exc_info()
            print("Exception Type: {}\nException Value: {}".format(exception_type,
                                                                   exception_value))


class UnitTestIdealData(unittest.TestCase):
    def test_loadDatas(self):
        idealData = IdealData()
        result = idealData.loadDatas()

        self.assertEqual(result.iloc[0]['y1'], -0.9129453)
