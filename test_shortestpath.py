import unittest
from Main import *
class TestShortestPath(unittest.TestCase):
    
    def test_shortest_path_exists(self):
        # 测试正常情况下存在路径的情况
        graph = Graph() 
        graph.add_edge("a", "b", 1)
        graph.add_edge("b", "c", 1)
        self.assertIn('a->b->c',graph.calcShortestPath("a", "c"))
    
    def test_start_or_end_not_in_graph(self):
        # 测试起始节点或目标节点不存在于图中的情况
        graph = Graph()
        graph.add_node("a")
        self.assertEqual(graph.calcShortestPath("a", "b"), ((), "No \"a\" or \"b\" in the graph!"))
    
    def test_only_one_node(self):
        # 测试只有一个节点的情况
        graph = Graph()
        graph.add_node("a")
        graph.add_node("b")
        graph.add_edge("a", "b", 1)
        self.assertEqual(({'a': 0, 'b': 1}, {'a': ['a'], 'b': ['a', 'b']}), graph.calcShortestPath("a",None))
        
    def test_same_start_and_end_node(self):
        # 测试起始节点和目标节点相同但不存在于图中的情况
        graph = Graph()
        graph.add_node("a")
        self.assertEqual(graph.calcShortestPath("a", "a"), ((), "No path from \"a\" to \"a\"!"))
    
    def test_no_path(self):
        # 测试不存在路径的情况
        graph = Graph()
        graph.add_node("a")
        graph.add_node("b")
        self.assertEqual(graph.calcShortestPath("a", "b"), ((), "No path from \"a\" to \"b\"!"))    

    def test_one_node(self):
        # 测试只有一个节点输入的情况
        graph = Graph()
        graph.add_node("a")
        self.assertEqual(graph.calcShortestPath("b", None), ((), 'No "b" in the graph!'))

if __name__ == "__main__":
    unittest.main(verbosity=2)