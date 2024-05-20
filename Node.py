import re
import networkx as nx
import matplotlib.pyplot as plt
import random
import heapq
import time
from UI.main_window import qt_start
from graphviz import Digraph

class Node():
    def __init__(self, text):
        self.text = text
        self.neighbors = {}
    
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
            words = re.sub(r'[^a-zA-z \n]', '', text)
            words = re.findall(r'\b\w+\b', words)
            for i in range(len(words) - 1):
                self.add_edge(words[i], words[i + 1])

    def print_graph(self):

        # 创建一个有向图
        self.G = Digraph()

        # 添加节点和边
        for node_text, node in self.nodes.items():
            self.G.node(node_text)
            for neighbor, weight in node.neighbors.items():
                self.G.edge(node_text, neighbor.text, label=str(weight))

        # 设置Graphviz布局
        self.G.engine = 'dot'

        # 保存图形为PNG文件
        self.G.render('graph', format='png', cleanup=True)
        
    # 用于判断是否可达，返回True or False
    def bfs(self, start, end):
        start = start.lower()
        end = end.lower()
        start_node = self.nodes.get(start)
        end_node = self.nodes.get(end)
        if not start_node or not end_node:
            print(f'No \"{start}\" or \"{end}\" in the graph!')
            return False
        queue = []  # 创建一个队列
        # 邻居都加入到这个搜索队列中
        for neighbor in start_node.neighbors:
            queue.append(neighbor.text)
        while queue:
            # 把可达队列打印出来
            print(queue)
            head_text = queue.pop(0)
            head_node = self.nodes.get(head_text)
            if head_text == end:
                return True
            else:
                for neighbor in head_node.neighbors:
                    queue.append(neighbor.text)
        if start == end:
            print("The same end with start!")
            return False
        print("Unreachable!")
        return False

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
            if len(path) == 1:
                return f'The bridge words from \"{start}\" to \"{end}\" is:' + path[0]
            else:
                return (f'The bridge words from \"{start}\" to \"{end}\" are:' + ','.join(path[:-1]) + ' and ' + path[-1])
        else:
            print(f'No bridge words from \"{start}\" to \"{end}\"!')
            return f'No bridge words from \"{start}\" to \"{end}\"!'

    def generate_sentence(self, s):
        if(s == ' ' or s == ''):
            return 'No input!'
        words = s.split()
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

    def getph(self):
        ph = {}
        for key in list(self.nodes.keys()):
            ph[key] = ph.get(key, {})
            for nei in self.nodes.get(key).neighbors:
                ph[key][nei.text] = self.nodes.get(key).neighbors[nei]
        return ph

    # ph就是图的邻居表示
    def dijksa(self, ph, *args):
        #可变参数，第一个为开始
        start = str(args[0])
        # 初始化距离表，所有节点的距离都是无限大
        distances = {node: float('infinity') for node in ph}
        # 初始化前驱节点表
        predecessors = {node: None for node in ph}
        # 设置起始节点的距离为0
        distances[start] = 0
        # 初始化优先队列
        priority_queue = [(0, start)]

        while priority_queue:
            # 取出队列中距离最小的节点
            current_distance, current_node = heapq.heappop(priority_queue)
            # 如果这个节点的距离已经不是最小了，那么跳过
            if current_distance > distances[current_node]:
                continue
            # 遍历当前节点的邻居
            for neighbor, weight in ph[current_node].items():
                distance = current_distance + weight
                # 如果计算出的距离比已知的小，那么更新距离表，并将邻居节点加入优先队列
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    predecessors[neighbor] = current_node
                    heapq.heappush(priority_queue, (distance, neighbor))

        # 构建最短路径
        paths = {}
        for node in ph:
            path = []
            current = node
            while current is not None:
                path.insert(0, current)
                current = predecessors[current]
            paths[node] = path
        if len(args) > 1:
            end = str(args[1])
            end = end.lower()
            print(f"Shortest path length from \"{start}\" to \"{end}\" is {distances[end]}")
            print(f"The path is {paths[end]}")
            # 设置正常边的颜色
            self.G = Digraph()

            # 添加节点和边
            for node_text, node in self.nodes.items():
                self.G.node(node_text)
                for neighbor, weight in node.neighbors.items():
                    # 设置边的默认颜色
                    edge_color = 'gray'
                    # 检查是否需要高亮边
                    if (node_text, neighbor.text) in [(paths[end][i], paths[end][i+1]) for i in range(len(paths[end])-1)]:
                        edge_color = 'red'
                    self.G.edge(node_text, neighbor.text, label=str(weight), color=edge_color, penwidth='2.0')

            # 设置Graphviz布局，使用与之前相同的布局
            self.G.engine = 'dot'
            self.G.graph_attr['layout'] = 'dot'

            # 保存图形为PNG文件
            self.G.render('graph', format='png', cleanup=True)
            return f"最短路径长度为 {distances[end]}"+'\n'+f"路径为 {'->'.join(paths[end])}"
        else:
            print("All min distances:")
            print(distances)    
            print("All paths as follows:")
            for key in paths.keys():
                print(key,end=':')
                print(paths[key])
        return distances, paths


    def shortest_path(self, *args):
        if len(args) > 1:
            start = str(args[0])
            end = str(args[1])
            start_node = self.nodes.get(start)
            end_node = self.nodes.get(end)
            if not start_node or not end_node:
                print(f'No \"{start}\" or \"{end}\" in the graph!')
                return (),(f'No \"{start}\" or \"{end}\" in the graph!')

            if not self.bfs(start, end):
                return (),(f'No path from \"{start}\" to \"{end}\"!')

            ph = self.getph()
            return self.dijksa(ph, start, end)
        else:
            start = str(args[0])
            start_node = self.nodes.get(start)
            if not start_node :
                print(f'No \"{start}\" in the graph!')
                return (),(f'No \"{start}\" in the graph!')
            ph = self.getph()
            return self.dijksa(ph, start)


    def random_traversal(self,graph):
        try:
            start_node = random.choice(list(graph.keys()))
            current_node = start_node
            visited_edges = set()
            traversal_path = [current_node]

            while True:
                if self.stop:
                    print("Random walk stopped")
                    break
                neighbors = list(graph[current_node].keys())
                if not neighbors:
                    break
                random_edge = random.choice(neighbors)
                if (current_node, random_edge) in visited_edges:
                    break
                visited_edges.add((current_node, random_edge))
                current_node = random_edge
                traversal_path.append(current_node)
                #time.sleep(0.5)

            return traversal_path
        except Exception as e:
            return ["Please input a graph first!"]
    def random_walk(self):
        self.done = False
        ph = self.getph()
        traversal_result = self.random_traversal(ph)

        # 将遍历的节点输出到txt文本文件
        with open('traversal_path.txt', 'w') as file:
            for node in traversal_result:
                file.write(node + '\n')

        print("Traversal path has been written to traversal_path.txt")
        self.done = True
        return "Done"


def showDirectedGraph():
    graph.print_graph()


def queryBridgeWords(word1, word2):
    return graph.query(word1, word2)


def generateNewText(s):
    return graph.generate_sentence(s)


def calcShortestPath(*args):
    return graph.shortest_path(*args)


def randomWalk():
    graph.random_walk()


graph = Graph()
qt_start(graph)