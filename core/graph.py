class Graph:
    def __init__(self):
        self.nodes = set()
        self.adj = {} # Dictionary of Dictionaries

    def add_node(self, node_id):
        self.nodes.add(node_id)
        if node_id not in self.adj:
            self.adj[node_id] = {}

    def add_edge(self, u, v, distance, time_list):
        # time_list là mảng 24 phần tử
        self.add_node(u)
        self.add_node(v)
        self.adj[u][v] = {'distance': distance, 'time_list': time_list}
        self.adj[v][u] = {'distance': distance, 'time_list': time_list} # Đồ thị vô hướng