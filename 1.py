from graphviz import Digraph

def draw_shortest_path_flow_chart():
    dot = Digraph()

    # 设置默认字体以支持中文显示
    dot.attr(fontname='Microsoft YaHei')

    # 函数入口
    dot.node('B1', 'B1', shape='circle', fontname='Microsoft YaHei')

    # 初始化变量
    dot.node('B2', 'B2', shape='circle', fontname='Microsoft YaHei')

    # 判断 len(args) > 1
    dot.node('B3', 'B3', shape='circle', fontname='Microsoft YaHei')

    # 判断 start_node 或 end_node 是否存在
    dot.node('B4', 'B4', shape='circle', fontname='Microsoft YaHei')

    # 没有开始或结束节点
    dot.node('B5', 'B5', shape='circle', fontname='Microsoft YaHei')

    # 调用 bfs 判断路径是否存在
    dot.node('B6', 'B6', shape='circle', fontname='Microsoft YaHei')

    # 无路径
    dot.node('B7', 'B7', shape='circle', fontname='Microsoft YaHei')


    # 调用 dijkstra 获取最短路径
    dot.node('B8', 'B8', shape='circle', fontname='Microsoft YaHei')

    # 初始化起始节点
    dot.node('B9', 'B9', shape='circle', fontname='Microsoft YaHei')

    # 判断起始节点是否存在
    dot.node('B10', 'B10', shape='circle', fontname='Microsoft YaHei')

    # 无开始节点
    dot.node('B11', 'B11', shape='circle', fontname='Microsoft YaHei')

    # 调用 dijkstra 获取所有节点到起始节点的最短路径
    dot.node('B12', 'B12', shape='circle', fontname='Microsoft YaHei')

    # 函数出口
    dot.node('B13', 'B13', shape='circle', fontname='Microsoft YaHei')

    # 添加边
    dot.edge('B1', 'B3')
    dot.edge('B3', 'B2')
    dot.edge('B3', 'B9')
    dot.edge('B2', 'B4')
    dot.edge('B4', 'B5')
    dot.edge('B4', 'B6')
    dot.edge('B6', 'B7')
    dot.edge('B6', 'B8')
    dot.edge('B5', 'B13')
    dot.edge('B7', 'B13')
    dot.edge('B8', 'B13')
    dot.edge('B9', 'B10')
    dot.edge('B10', 'B11')
    dot.edge('B10', 'B12')
    dot.edge('B11', 'B13')
    dot.edge('B12', 'B13')

    # 设置直角边
    dot.attr('edge', splines='ortho')

    dot.render('control_flow', format='png', cleanup=True)

draw_shortest_path_flow_chart()
