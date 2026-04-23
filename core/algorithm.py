from utility.heap import MinHeap

def dijkstra(graph, start, end, mode='distance', hour=0, avoid_nodes=None, avoid_edges=None):
    if avoid_nodes is None: avoid_nodes = set()
    if avoid_edges is None: avoid_edges = set()

    distances = {node: float('inf') for node in graph.nodes}
    previous = {node: None for node in graph.nodes}
    distances[start] = 0
    
    pq = MinHeap()
    pq.push((0, start))

    while not pq.is_empty():
        current_cost, u = pq.pop()

        if u == end: break
        if current_cost > distances[u]: continue

        for v, data in graph.adj.get(u, {}).items():
            # Constraints: Avoid nodes/edges
            if v in avoid_nodes: continue
            if (u, v) in avoid_edges or (v, u) in avoid_edges: continue

            # Select weight based on criteria
            weight = data['distance'] if mode == 'distance' else data['time_list'][hour]
            
            new_dist = current_cost + weight
            if new_dist < distances[v]:
                distances[v] = new_dist
                previous[v] = u
                pq.push((new_dist, v))

    # Path Reconstruction
    path, curr = [], end
    if distances[end] == float('inf'): return None, 0, 0
    
    while curr:
        path.append(curr)
        curr = previous[curr]
    path.reverse()

    # Calculate totals
    total_d, total_t = 0, 0
    for i in range(len(path) - 1):
        edge = graph.adj[path[i]][path[i+1]]
        total_d += edge['distance']
        total_t += edge['time_list'][hour]

    return path, total_d, total_t