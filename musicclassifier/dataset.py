import numpy as np
import pandas as pd
import seaborn as sns; sns.set()
from sklearn.utils import shuffle
class Dataset():
    def __init__(self, file='./data/music_data.csv'):
        self.data = pd.read_csv('./data/music_data.csv')
        self.data = self.data.drop(columns='filename')
        self.features = list(self.data.columns)

    def shuffle(self):
        return shuffle(self.data)

    def split_data(self, folds=2):
        self.data = self.shuffle()
        mask = np.random.rand(len(self.data)) < (1. / folds)
        train_x = self.data[mask]
        test_x = self.data[~mask]
        train_target = train_x.loc[:, 'label']
        test_target = test_x.loc[:, 'label']
        train_x = train_x.drop(columns=['label'], axis=1)
        test_x = test_x.drop(columns=['label'], axis=1)
        return train_x, test_x, train_target, test_target
