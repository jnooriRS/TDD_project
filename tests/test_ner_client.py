import unittest
from ner_client import NamedEntityClient


class TestNerClient(unittest.TestCase):
    def test__gets_ents_returns_dictionary_given_empty_string(self):
        ner = NamedEntityClient()
        ents = ner.get_entity("")
        self.assertIsInstance(ents, dict)
