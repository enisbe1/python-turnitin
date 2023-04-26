import pandas as pd
import math
from connection import Connection


def print_factors(x):
    print("The factors of", x, "are:")
    for i in range(1, x + 1):
        if x % i == 0:
            print(i)


class TestData(Connection):
    def __init__(self, idealFunctions):
        self.idealFunctions = idealFunctions
        super().__init__()

    def createTable(self):
        self.base.metadata.create_all(self.engine)

    def initializeDatas(self, data):
        print('testttt', data)
        data.to_sql('test_data_deviation', self.engine,
                    if_exists='replace', index=False)

    def compare(self):
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
