from idealFunctions import IdealFunctions
from testData import TestData


def main():
    idealFunctions = IdealFunctions()
    testData = TestData(idealFunctions.findFunctions())
    datasToSave = testData.compare()
    testData.initializeDatas(datasToSave)


if __name__ == '__main__':
    main()
