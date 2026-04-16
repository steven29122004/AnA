class Pathfinder:
    def __init__(self, graph, nodes):
        self.graph = graph
        self.nodes = nodes

    def find_path(self, start, end, hour, mode, avoid_nodes=None, avoid_edges=None):
        raise NotImplementedError("Phải cài đặt hàm này ở class con.")