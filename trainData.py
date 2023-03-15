from connection import Connection
import pandas as pd


class TrainData(Connection):
    def __init__(self):
        super().__init__()

    def createTable(self):
        self.base.metadata.create_all(self.engine)

    def initializeDatas(self):
        df = pd.read_csv('dataset/train.csv')
        super().dropTable()
        self.createTable()
        df.to_sql('train_data', self.engine, if_exists='replace', index=False)

    def loadDatas(self):
        return pd.read_sql_table(
            'train_data', self.engine.connect())
