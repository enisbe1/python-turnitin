from trainData import TrainData
from idealData import IdealData
import numpy as np


def main():
    trainData = TrainData()
    trainData.initializeDatas()
    idealData = IdealData()
    idealData.initializeDatas()
    trainDf = trainData.loadDatas()
    print('trainDf', trainDf)
    idealDf = idealData.loadDatas()

    trainCols = ['x', 'y1', 'y2', 'y3', 'y4']
    trainArray = np.array(trainDf[trainCols])
    idealArray = np.array(idealDf)
    coefficients, _, _, _ = np.linalg.lstsq(
        trainArray, idealArray, rcond=None)
    ideal_functions = coefficients.T
    print(ideal_functions)


if __name__ == '__main__':
    main()
