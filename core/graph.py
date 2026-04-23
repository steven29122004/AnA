class Node:
    def __init__(self, node_id, x=0.0, y=0.0):
        self.node_id = node_id
        self.x = x
        self.y = y

class Edge:
    def __init__(self, destination, distance, times):
        self.destination = destination
        self.distance = distance
        self.time = times  # List 24 phần tử (24h)

    def get_time(self, hour):
        return self.time[hour]

    def update_times(self, new_times):
        self.time = new_times

class Graph:
    def __init__(self):
        self._nodes = {}  # { node_id -> Node }
        self._adj = {}    # { node_id -> list[Edge] }

    def add_node(self, node_id, x=0.0, y=0.0):
        if node_id not in self._nodes:
            self._nodes[node_id] = Node(node_id, x, y)
            self._adj[node_id] = []

    def add_edge(self, u, v, distance, times):
        # Đảm bảo 2 node tồn tại
        if u not in self._nodes:
            self.add_node(u)
        if v not in self._nodes:
            self.add_node(v)
        
        # Thêm cạnh 2 chiều (Bidirectional) cho đường bộ
        self._adj[u].append(Edge(v, distance, times))
        self._adj[v].append(Edge(u, distance, times))

    def get_neighbors(self, node_id, avoid_nodes=None, avoid_edges=None):
        if avoid_nodes is None:
            avoid_nodes = set()
        if avoid_edges is None:
            avoid_edges = set()
            
        neighbors = []
        for edge in self._adj.get(node_id, []):
            v = edge.destination
            # Lọc Node và Cạnh bị cấm
            if v in avoid_nodes:
                continue
            if tuple(sorted([node_id, v])) in avoid_edges:
                continue
            neighbors.append(edge)
            
        return neighbors

    def get_node(self, node_id):
        """Return the Node object for node_id, or None if not found."""
        return self._nodes.get(node_id, None)

    def has_node(self, node_id):
        """Return True if node_id exists in the graph."""
        return node_id in self._nodes

    def has_edge(self, u, v):
        """Return True if a direct edge from u to v exists."""
        for edge in self._adj.get(u, []):
            if edge.destination == v:
                return True
        return False