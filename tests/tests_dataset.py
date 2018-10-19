import unittest
from musicclassifier.dataset import Dataset

class Test_Dataset(unittest.TestCase):
    def setUp(self):
        self.dataset = Dataset()

    def test_dataset_exists(self):
        self.assertIsNotNone(self.dataset)
