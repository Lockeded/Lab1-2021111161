import unittest
from Main import *

class TestQueryBridgeWords(unittest.TestCase):

    def setUp(self):
        # Create a graph and add some nodes and edges for testing
        self.graph = Graph()
        self.graph.add_edge("hello", "there")
        self.graph.add_edge("there", "world")
        self.graph.add_edge("good", "morning")

    def test_bridge_words_exist(self):
        result = self.graph.query("hello", "world")
        print(f"test_bridge_words_exist: {result}")
        self.assertEqual(result, 'The bridge words from "hello" to "world" is: there')

    def test_no_bridge_words(self):
        result = self.graph.query("good", "morning")
        print(f"test_no_bridge_words: {result}")
        self.assertEqual(result, 'No bridge words from "good" to "morning"!')

    def test_word1_not_in_graph(self):
        result = self.graph.query("nonexistent", "world")
        print(f"test_word1_not_in_graph: {result}")
        self.assertEqual(result, 'No "nonexistent" in the graph!')

    def test_word2_not_in_graph(self):
        result = self.graph.query("hello", "nonexistent")
        print(f"test_word2_not_in_graph: {result}")
        self.assertEqual(result, 'No "nonexistent" in the graph!')

    def test_both_words_not_in_graph(self):
        result = self.graph.query("nonexistent1", "nonexistent2")
        print(f"test_both_words_not_in_graph: {result}")
        self.assertEqual(result, 'No "nonexistent1" and "nonexistent2" in the graph!')

    def test_same_word(self):
        result = self.graph.query("hello", "hello")
        print(f"test_same_word: {result}")
        self.assertEqual(result, 'No bridge words from "hello" to "hello"!')

    def test_empty_strings(self):
        result = self.graph.query("", "")
        print(f"test_empty_strings: {result}")
        self.assertEqual(result, 'No "" and "" in the graph!')

    def test_none_input(self):
        result = self.graph.query(None, None)
        print(f"test_none_input: {result}")
        self.assertEqual(result, 'No "None" and "None" in the graph!')

if __name__ == "__main__":
    unittest.main(verbosity=2)
