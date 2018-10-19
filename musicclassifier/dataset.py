import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns; sns.set()
from sklearn.utils import shuffle
class Dataset():
    def __init__(self, file='./data/music_data.csv'):
        self.data = pd.read_csv('./data/music_data.csv')
        self.data = shuffle(self.data)
        self.features = list(self.data.columns)
        self.features.remove('filename')
    def plot_features(self):
        # for f in self.features[0:-1]:
        #     figure, axis = plt.subplots(figsize=(20, 10))
        #     axis.tick_params(axis='both', which='major', labelsize=16)
        #     sns.barplot(data=self.data, x='label', y=f)
        # plt.show()
        return True
