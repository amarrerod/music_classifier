
import unittest
from musicclassifier.classifiers import MusicClassifier

class TestClassifier(unittest.TestCase):
    def setUp(self):
        self.classifier = MusicClassifier()
    def test_classifier_exists(self):
        self.assertIsNotNone(self.classifier)
