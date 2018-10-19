
from sklearn.naive_bayes import GaussianNB
import matplotlib.pyplot as plt
import seaborn as sns; sns.set()
import numpy as np

class MusicGaussianNB():
    def __init__(self, dataset = None):
        self.model = GaussianNB()
        self.dataset = dataset
        self.data = self.dataset.data
    def train(self, folds=2):
        if self.data is None:
            raise Exception("No data given yet")
        else:
            self.data = self.dataset.shuffle()
            mask = np.random.rand(len(self.data)) < (folds / 10.)
            self.train_x = self.data[mask]
            self.test_x = self.data[~mask]
            self.train_target = self.train_x.loc[:, 'label']
            self.test_target = self.test_x.loc[:, 'label']
            return True
