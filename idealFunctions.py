import pandas as pd
from trainData import TrainData
from idealData import IdealData
import numpy as np


class IdealFunctions:
    def __init__(self):
        pass

    def initializeDatas(self):
        trainData = TrainData()
        trainData.initializeDatas()
        idealData = IdealData()
        idealData.initializeDatas()

        trainDf = trainData.loadDatas()
        idealDf = idealData.loadDatas()

        return trainDf, idealDf

    def findFunctions(self):
        result = self.initializeDatas()
        trainDf, idealDf = result
        # Extract y values from training dataset
        train_y1 = trainDf['y1'].values
        train_y2 = trainDf['y2'].values
        train_y3 = trainDf['y3'].values
        train_y4 = trainDf['y4'].values

        ideal_x = idealDf['x'].values

        # Extract y values from ideal functions dataset
        ideal_y = idealDf.iloc[:, 1:].values

        deviations = np.zeros(50)

        for i in range(50):
            ideal_yi = ideal_y[:, i]
            A = np.vstack([train_y1, train_y2, train_y3, train_y4]).T
            b = ideal_yi
            x, _, _, _ = np.linalg.lstsq(A, b, rcond=None)
            deviations[i] = np.sum((np.dot(A, x) - b)**2)

        # Choose the four ideal functions with the smallest deviation
        idx = np.argsort(deviations)[:4]
        ideal_chosen = ideal_y[:, idx]

        frame = pd.DataFrame(ideal_chosen, columns=['y1', 'y2', 'y3', 'y4'])
        frame['x'] = ideal_x

        return frame, idealDf, trainDf
