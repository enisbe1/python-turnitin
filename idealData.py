from connection import Connection
import pandas as pd


class IdealData(Connection):

    def createTable(self):
        self.base.metadata.create_all(self.engine)

    def initializeDatas(self):
        df = pd.read_csv('dataset/ideal.csv')
        self.createTable()
        df.to_sql('ideal_data', self.engine, if_exists='replace', index=False)

    def loadDatas(self):
        return pd.read_sql_table(
            'ideal_data', self.engine.connect())
