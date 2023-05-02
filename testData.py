import sys
import pandas as pd
import math
from connection import Connection


class TestData(Connection):
    def __init__(self, idealFunctions):
        '''
        Constructor of this class
        idealFunctions: Ideal functions dataframe provided from previous calculation found best 4
        '''
        self.idealFunctions = idealFunctions
        super().__init__()

    def createTable(self):
        '''
        Creates database if not exists
        No argument provided
        Type void
        '''
        self.base.metadata.create_all(self.engine)

    def initializeDatas(self, data):
        '''
        Initializes datas on database as table test_data_deviation
        data: Data to be inserted after calculation are made(dataframe)
        Type void
        '''
        data.to_sql('test_data_deviation', self.engine,
                    if_exists='replace', index=False)

    def compare(self):
        '''
        Load test datas row by row and compares with idealFunctions to find if it passes
        No parameters provided
        Returns dataframe with the functions that passed the conditions
        '''
        try:
            testData = pd.read_csv('dataset/test.csv')
            datasPassed = []
            for index, row in testData.iterrows():
                found = self.idealFunctions[self.idealFunctions['x'] == row['x']]
                maxValue = found.filter(like='y').iloc[0].max()
                if row['y'] / maxValue <= math.sqrt(2):
                    rowAppended = {'x': row['x'], 'y': row['y'], 'delta_y': maxValue,
                                   'number_of_function': found.index[0]}
                    datasPassed.append(rowAppended)

            df = pd.DataFrame(datasPassed)
            return df
        except:
            exception_type, exception_value, exception_traceback = sys.exc_info()
            print("Exception Type: {}\nException Value: {}".format(exception_type,
                                                                   exception_value))
