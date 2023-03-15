from connection import Connection
import pandas as pd
from trainData import TrainData
from idealData import IdealData
import numpy as np


class IdealFunctions(Connection):
    def __init__(self):
        super().__init__()

    def createTable(self):
        self.base.metadata.create_all(self.engine)

    def insertDatas(self):
        result = self.initializeDatas()
        trainDf, idealDf = result

        idealFunctions = self.findFunctions(trainDf, idealDf)
        matrix = np.array(idealFunctions)
        data = {'x': matrix[:, 0], 'y1': matrix[:, 1],
                'y2': matrix[:, 2], 'y3': matrix[:, 3], 'y4': matrix[:, 4]}
        df = pd.DataFrame(data)
        df.to_sql('ideal_functions', self.engine,
                  if_exists='replace', index=False)

    def initializeDatas(self):
        trainData = TrainData()
        trainData.initializeDatas()
        idealData = IdealData()
        idealData.initializeDatas()

        trainDf = trainData.loadDatas()
        idealDf = idealData.loadDatas()

        return trainDf, idealDf

    def findFunctions(self, trainDf, idealDf):
        trainCols = ['x', 'y1', 'y2', 'y3', 'y4']
        trainArray = np.array(trainDf[trainCols])
        idealArray = np.array(idealDf)
        coefficients, _, _, _ = np.linalg.lstsq(
            trainArray, idealArray, rcond=None)
        ideal_functions = coefficients.T

        return ideal_functions

    def loadDatas(self):
        return pd.read_sql_table(
            'ideal_data', self.engine.connect())
