import re
import networkx as nx
import matplotlib.pyplot as plt
import random
from UI.main_window import qt_start
class Node():
    def __init__(self, text):
        self.text = text
        self.neighbors = {} 
        self.distance = {}
    def add_neighbor(self, neighbor, weight=1):
        self.neighbors[neighbor] = self.neighbors.get(neighbor, 0) + weight

class Graph():
    def __init__(self):
        self.nodes = {}

    def add_node(self, text):
        node = self.nodes.get(text)
        if not node:
            node = Node(text)
            self.nodes[text] = node
        return node

    def add_edge(self, source, target, weight=1):
        source_node = self.add_node(source)
        target_node = self.add_node(target)
        source_node.add_neighbor(target_node, weight)

    def read_txt(self, txt_file):
        with open(txt_file, 'r') as file:
            text = file.read().lower()
            words = re.sub(r'[^a-zA-z \n]','',text)
            words = re.findall(r'\b\w+\b', words)
            for i in range(len(words) - 1):
                self.add_edge(words[i], words[i + 1])

    def print_graph(self):
        G = nx.DiGraph()
        for node_text, node in self.nodes.items():
            G.add_node(node_text)
            for neighbor, weight in node.neighbors.items():
                G.add_edge(node_text, neighbor.text, weight=weight, arrows=True)
        pos = nx.fruchterman_reingold_layout(G)
        nx.draw_networkx(G,pos, with_labels=True,alpha=0.5, font_size = 8)
        labels = nx.get_edge_attributes(G,'weight')
        nx.draw_networkx_edge_labels(G,pos,edge_labels=labels)
        plt.savefig('graph.png')
        #plt.show()

    def dfs(self, start, end, path=[]):
        path = path + [start]
        if start == end:
            return path
        for node in start.neighbors:
            if node not in path:
                new_path = self.dfs(node, end, path)
                if new_path:
                    return new_path
        return None
    
    def query(self, start, end, generate=False):
        start = start.lower()
        end = end.lower()
        start_node = self.nodes.get(start)
        end_node = self.nodes.get(end)
        path = []
        if generate:
            if not start_node or not end_node:
                return
            for neighbor in start_node.neighbors:
                if end_node in neighbor.neighbors:
                    path.append(neighbor.text)
            return path
        if not start_node and not end_node:
            print(f'No \"{start}\" and \"{end}\" in the graph!')
            return f'No \"{start}\" and \"{end}\" in the graph!'
        if not start_node:
            print(f'No \"{start}\" in the graph!')
            return f'No \"{start}\" in the graph!'
        if not end_node:
            print(f'No \"{end}\" in the graph!')
            return f'No \"{end}\" in the graph!'
        for neighbor in start_node.neighbors:
                if end_node in neighbor.neighbors:
                    path.append(neighbor.text)
        if path:
            print(f'The bridge words from \"{start}\" to \"{end}\" are:', ' -> '.join(path))
            return ' '.join(path)
        else:
            print(f'No path found from \"{start}\" to \"{end}\"!')
            return f'No path found from \"{start}\" to \"{end}\"!'
            
    def generate_sentence(self,str):
        words = str.split()
        new_words = []
        for i in range(len(words) - 1):
            start = words[i]
            end = words[i + 1]
            bridge = self.query(start, end, True)
            new_words.append(words[i])
            if bridge:
                new_words.append(bridge[random.randint(0, len(bridge) - 1)])
        new_words.append(words[-1])
        sentence = ' '.join(new_words)
        print(sentence)
        return sentence
    
    def dikstra(self, start, end):
        distances = {}
        start_node = self.nodes.get(start)
        end_node = self.nodes.get(end)
        raise NotImplementedError
        

    def shortest_path(self, start, end):
        start_node = self.nodes.get(start)
        end_node = self.nodes.get(end)
        if not start_node or not end_node:
            print(f'No \"{start}\" or \"{end}\" in the graph!')
            return
        raise NotImplementedError
    
    def random_walk(self):
        raise NotImplementedError

def showDirectedGraph():
    graph.print_graph()

def queryBridgeWords(word1, word2):
    return graph.query(word1, word2)

def generateNewText(str):
    return graph.generate_sentence(str)

def calcShortestPath(word1, word2):
    return graph.shortest_path(word1, word2)

def randomWalk():
    graph.random_walk()


graph = Graph()
qt_start(graph)
# graph.read_txt('poet.txt')
# graph.generate_sentence('Seek to explore new and exciting synergies')