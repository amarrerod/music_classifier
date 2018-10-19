import unittest
from musicclassifier.dataset import Dataset

class Test_Dataset(unittest.TestCase):
    def setUp(self):
        self.dataset = Dataset()

    def test_dataset_exists(self):
        self.assertIsNotNone(self.dataset)
    def test_data_exists(self):
        self.assertIsNotNone(self.dataset.data)
    def test_data_has_features(self):
        self.assertIsNotNone(self.dataset.features)
    def test_data_features_are_29(self):
        self.assertEqual(29, len(self.dataset.features))
    def test_data_show_plots_True(self):
        self.assertTrue(self.dataset.plot_features())
    def test_data_rows_are_1001(self):
        self.assertTrue(1001, len(self.dataset.data))
    def test_data_shuffle(self):
        self.assertEqual(len(self.dataset.shuffle()), len(self.dataset.data))
