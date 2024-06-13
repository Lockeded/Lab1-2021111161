from graphviz import Digraph

def draw_shortest_path_flow_chart():
    dot = Digraph()

    # 设置默认字体以支持中文显示
    dot.attr(fontname='Microsoft YaHei')

    # 函数入口
    dot.node('start', '开始', shape='ellipse', fontname='Microsoft YaHei')

    # 初始化变量
    dot.node('B1', 'start=str(args[0])\nend=str(args[1])\nstart_node=self.nodes.get(start)\nend_node=self.nodes.get(end)', shape='box', fontname='Microsoft YaHei')

    # 判断 len(args) > 1
    dot.node('B2', 'len(args) > 1', shape='diamond', fontname='Microsoft YaHei')

    # 判断 start_node 或 end_node 是否存在
    dot.node('B3', 'not start_node or not end_node', shape='diamond', fontname='Microsoft YaHei')

    # 没有开始或结束节点
    dot.node('B4', 'No \"start\" or \"end\" in the graph!', shape='box', fontname='Microsoft YaHei')

    # 调用 bfs 判断路径是否存在
    dot.node('B5', 'not self.bfs(start, end)', shape='diamond', fontname='Microsoft YaHei')

    # 无路径
    dot.node('B6', 'No path from \"start\" to \"end\"!', shape='box', fontname='Microsoft YaHei')


    # 调用 dijkstra 获取最短路径
    dot.node('B8', 'ph = self.getph() \n return self.dijksa(ph, start, end)', shape='box', fontname='Microsoft YaHei')

    # 初始化起始节点
    dot.node('B9', 'start=str(args[0])\nstart_node=self.nodes.get(start)', shape='box', fontname='Microsoft YaHei')

    # 判断起始节点是否存在
    dot.node('B10', 'not start_node', shape='diamond', fontname='Microsoft YaHei')

    # 无开始节点
    dot.node('B11', 'No \"start\" in the graph!', shape='box', fontname='Microsoft YaHei')

    # 调用 dijkstra 获取所有节点到起始节点的最短路径
    dot.node('B12', 'ph = self.getph() \n return self.dijksa(ph, start)', shape='box', fontname='Microsoft YaHei')

    # 函数出口
    dot.node('end', '返回', shape='ellipse', fontname='Microsoft YaHei')

    # 添加边
    dot.edge('start', 'B2', fontname='Microsoft YaHei')
    dot.edge('B2', 'B1', label='T', fontname='Microsoft YaHei')
    dot.edge('B2', 'B9', label='F', fontname='Microsoft YaHei')
    dot.edge('B1', 'B3', fontname='Microsoft YaHei')
    dot.edge('B3', 'B4', label='T', fontname='Microsoft YaHei')
    dot.edge('B3', 'B5', label='F', fontname='Microsoft YaHei')
    dot.edge('B5', 'B6', label='T', fontname='Microsoft YaHei')
    dot.edge('B5', 'B8', label='F', fontname='Microsoft YaHei')
    dot.edge('B4', 'end', fontname='Microsoft YaHei')
    dot.edge('B6', 'end', fontname='Microsoft YaHei')
    dot.edge('B8', 'end', fontname='Microsoft YaHei')
    dot.edge('B9', 'B10', fontname='Microsoft YaHei')
    dot.edge('B10', 'B11', label='T', fontname='Microsoft YaHei')
    dot.edge('B10', 'B12', label='F', fontname='Microsoft YaHei')
    dot.edge('B11', 'end', fontname='Microsoft YaHei')
    dot.edge('B12', 'end', fontname='Microsoft YaHei')

    # 设置直角边
    dot.attr('edge', splines='ortho')

    dot.render('shortest_path_flow_chart', format='png', cleanup=True)

draw_shortest_path_flow_chart()
