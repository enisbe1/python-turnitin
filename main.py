from idealFunctions import IdealFunctions
from testData import TestData
from visualization import Vizualization
from bokeh.plotting import figure, output_file, show
from bokeh.layouts import column
from bokeh.models import ColumnDataSource
output_file("layout.html")


def main():
    '''
    Main method to start the application
    Calls classes with logical order to execute each one of them
    On program execution this method is called
    No return on this method
    '''
    idealFunctions = IdealFunctions()
    frame, idealDf, trainDf = idealFunctions.findFunctions()
    testData = TestData(frame)
    datasToSave = testData.compare()

    visualization = Vizualization(trainDf, idealDf, frame, datasToSave)
    visualization.vizualize()


if __name__ == '__main__':
    main()
