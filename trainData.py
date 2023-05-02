import sys
from connection import Connection
import pandas as pd
import unittest


class TrainData(Connection):
    def __init__(self):
        '''
        Constructor of this class
        It initialises base class Connection
        '''
        super().__init__()

    def createTable(self):
        '''
        Creates database if not exists
        No parameter provided
        Type void
        '''
        self.base.metadata.create_all(self.engine)

    def initializeDatas(self):
        '''
        Initializes datas on database under table train data by reading train.csv under dataset folder
        No parameter provided
        Void method
        '''
        try:
            df = pd.read_csv('dataset/train.csv')
            super().dropTable()
            self.createTable()
            df.to_sql('train_data', self.engine,
                      if_exists='replace', index=False)
        except:
            exception_type, exception_value, exception_traceback = sys.exc_info()
            print("Exception Type: {}\nException Value: {}".format(exception_type,
                                                                   exception_value))

    def loadDatas(self):
        '''
        Loads data from train_data table
        No parameter provided
        Returns train_data table with the rows it contains as dataframe
        '''
        try:
            return pd.read_sql_table(
                'train_data', self.engine.connect())
        except:
            exception_type, exception_value, exception_traceback = sys.exc_info()
            print("Exception Type: {}\nException Value: {}".format(exception_type,
                                                                   exception_value))


class UnitTestTrainData(unittest.TestCase):
    def test_loadDatas(self):
        trainData = TrainData()
        trainData.initializeDatas()
        result = trainData.loadDatas()
        self.assertEqual(result.iloc[0]['x'], -20)


if __name__ == '__main__':
    unittest.main()
