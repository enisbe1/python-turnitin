import sys
from bokeh.plotting import figure, output_file, show
from bokeh.layouts import column
from bokeh.models import ColumnDataSource
output_file("layout.html")
colors = ['red', 'green', 'blue', 'yellow', 'purple']


class Vizualization:
    def __init__(self, trainDf, idealDf, frame, datasToSave):
        '''
        Constructor of this class, initializes the parameters provided when called
        trainDf: Train dataset loaded from database
        idealDf: Ideal dataset loaded from database
        frame: Datas calculated as maximum deviation
        datasToSave: Compared with test data and only the fitted ones in calculations
        '''
        self.trainDf = trainDf
        self.idealDf = idealDf
        self.frame = frame
        self.datasToSave = datasToSave
        pass

    def visualizeFrame(self, dtFrame, title):
        '''
        It visualizes a single frame using bokeh
        dtFrame: Dataframe for visualization with circles
        title: Title for the dataframe
        Return the graph created by given dataframe
        '''
        try:
            source = ColumnDataSource(dtFrame)
            p = figure(title=title,
                       x_axis_label='X', y_axis_label='Y')
            for i, col in enumerate(dtFrame.columns[1:]):
                p.circle('x', col, source=source,
                         color=colors[i % 5], size=1)

            return p
        except:
            exception_type, exception_value, exception_traceback = sys.exc_info()
            print("Exception Type: {}\nException Value: {}".format(exception_type,
                                                                   exception_value))

    def vizualize(self):
        '''
        Vizualizes the graphs in column
        No parameters provided
        Type void
        '''
        try:
            trainGraph = self.visualizeFrame(self.trainDf, 'Train Data')
            idealGraph = self.visualizeFrame(self.idealDf, 'Ideal Data')
            frameGraph = self.visualizeFrame(self.frame, 'Ideal Functions')
            datasToSaveGraph = self.visualizeFrame(self.frame, 'Ideal Data')

            show(column(trainGraph, idealGraph, frameGraph, datasToSaveGraph))
        except:
            exception_type, exception_value, exception_traceback = sys.exc_info()
            print("Exception Type: {}\nException Value: {}".format(exception_type,
                                                                   exception_value))
