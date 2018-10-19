
import unittest
from musicclassifier.classifiers import MusicGaussianNB
from musicclassifier.dataset import Dataset

class TestGaussianNB(unittest.TestCase):
    def setUp(self):
        self.dataset = Dataset()
        self.classifier = MusicGaussianNB(self.dataset)
    def test_classifier_exists(self):
        self.assertIsNotNone(self.classifier)
    def test_classifier_has_data(self):
        self.assertEqual(len(self.dataset.data), len(self.classifier.data))
    def test_classifier_trains(self):
        self.assertTrue(self.classifier.train())
