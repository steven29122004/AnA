"""
FILE: Core/algorithm.py
AUTHOR: Nhan
DESCRIPTION: A* algorithm implementation for finding the shortest path based on distance.
"""

from Utility.heap import MinHeap

def get_heuristic(node_coords, current_node, goal_node):
    """Calculates Euclidean distance between two nodes."""
    (x1, y1) = node_coords[current_node]
    (x2, y2) = node_coords[goal_node]
    return ((x1 - x2)**2 + (y1 - y2)**2)**0.5

def a_star_distance(graph_obj, start, goal, avoid_nodes=None, avoid_edges=None):
    """
    Finds the shortest path based on fixed distance.
    Returns: (path_list, total_distance)
    """
    # Initialize constraints
    avoid_nodes = set(avoid_nodes) if avoid_nodes else set()
    avoid_edges = set(avoid_edges) if avoid_edges else set()

    pq = MinHeap()
    pq.push((0, start)) # (f_score, node)
    
    came_from = {start: None}
    g_score = {start: 0} # Actual distance from start to current node

    while not pq.is_empty():
        result = pq.pop()
        if result is None: break
        
        _, current = result

        if current == goal:
            return reconstruct_path(came_from, current), g_score[current]

        # Iterate through neighbors in the adjacency list
        # Assuming neighbor_info is (distance, [24_hours_time_list])
        for neighbor, info in graph_obj.adjacency_list[current].items():
            distance = info[0]

            # Check for avoid lists
            if neighbor in avoid_nodes or (current, neighbor) in avoid_edges:
                continue
            
            tentative_g_score = g_score[current] + distance
            
            if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
                g_score[neighbor] = tentative_g_score
                # f(n) = g(n) + h(n)
                f_score = tentative_g_score + get_heuristic(graph_obj.node_coords, neighbor, goal)
                came_from[neighbor] = current
                pq.push((f_score, neighbor))

    return None, float('inf')

def reconstruct_path(came_from, current):
    """Backtracks from goal to start to retrieve the path."""
    path = []
    while current is not None:
        path.append(current)
        current = came_from.get(current)
    return path[::-1]