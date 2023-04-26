from idealFunctions import IdealFunctions
from testData import TestData


def main():
    idealFunctions = IdealFunctions()
    testData = TestData(idealFunctions.findFunctions())
    testData.compare()


if __name__ == '__main__':
    main()
