from bokeh.plotting import figure, output_file, show
from bokeh.layouts import column
from bokeh.models import ColumnDataSource
output_file("layout.html")
colors = ['red', 'green', 'blue', 'yellow', 'purple']


class Vizualization:
    def __init__(self, trainDf, idealDf, frame, datasToSave):
        self.trainDf = trainDf
        self.idealDf = idealDf
        self.frame = frame
        self.datasToSave = datasToSave
        pass

    def visualizeFrame(self, dtFrame, title):
        source = ColumnDataSource(dtFrame)
        p = figure(title=title,
                   x_axis_label='X', y_axis_label='Y')
        for i, col in enumerate(dtFrame.columns[1:]):
            p.circle('x', col, source=source,
                     color=colors[i % 5], size=1)

        return p

    def vizualize(self):
        trainGraph = self.visualizeFrame(self.trainDf, 'Train Data')
        idealGraph = self.visualizeFrame(self.idealDf, 'Ideal Data')
        frameGraph = self.visualizeFrame(self.frame, 'Ideal Functions')
        datasToSaveGraph = self.visualizeFrame(self.frame, 'Ideal Data')

        show(column(trainGraph, idealGraph, frameGraph, datasToSaveGraph))
