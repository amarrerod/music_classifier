
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score
import seaborn as sns; sns.set()

class MusicGaussianNB():
    def __init__(self, dataset = None):
        self.model = GaussianNB()
        self.dataset = dataset
        self.data = self.dataset.data
    def train(self, folds=2):
        if self.data is None:
            raise Exception("No data given yet")
        else:
            self.train_x, self.test_x, self.train_y, self.test_y = self.dataset.split_data(folds)
            self.model.fit(self.train_x, self.train_y)
            y_model = self.model.predict(self.test_x)
            print("Precission: {}".format(accuracy_score(y_model, self.test_y)))
            return True
