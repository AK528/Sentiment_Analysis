import pandas as pd
from sentiment_analysis.config import dataset , DATAFILE

class DataLoader:
    def __init__(self):
        self.data = [
            pd.read_csv(
                 DATAFILE + "{}".format(f))
            for f in dataset

        ]

    def load(self, predict_on=None):
        if predict_on is None:
            return self.data
        else:
            data = pd.read_csv(predict_on)
            return data

if __name__=='__main__':
    dataset = DataLoader().load()
    print(dataset)