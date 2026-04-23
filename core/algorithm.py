import math
from utility.heap import MinHeap

def heuristic(graph, current_id, goal_id, mode):
    """
    1. Implement heuristic function
    Tính khoảng cách đường chim bay (Euclidean distance) giữa 2 điểm.
    """
    curr = graph.get_node(current_id)
    goal = graph.get_node(goal_id)
    if not curr or not goal:
        return 0.0

    # Khoảng cách Euclide
    dx = curr.x - goal.x
    dy = curr.y - goal.y
    dist = math.sqrt(dx*dx + dy*dy)

    if mode == 'distance':
        return dist
    elif mode == 'time':
        # Giả định tốc độ trung bình max là 1 đơn vị khoảng cách / 0.1 phút
        # Để đảm bảo heuristic "admissible" (không đánh giá cao hơn thực tế)
        return dist * 0.1 
        
    return 0.0

def a_star(graph, start, end, mode='distance', hour=0, avoid_nodes=None, avoid_edges=None):
    """
    2 & 3. Implement A* for shortest path and fastest time
    """
    if avoid_nodes is None: avoid_nodes = set()
    if avoid_edges is None: avoid_edges = set()

    # Sử dụng class MinHeap của leader
    pq = MinHeap()
    counter = 0  # Dùng để tie-break (xử lý trùng lặp giá trị f_score)
    
    # Node đầu tiên: (f_score, counter, node_id)
    pq.insert((0, counter, start))
    
    g_score = {start: 0.0}
    dist_total = {start: 0.0}
    time_total = {start: 0.0}
    came_from = {}

    while len(pq.heap) > 0:
        # Lấy phần tử nhỏ nhất từ Heap
        current_f, _, current_node = pq.extract_min()

        # Nếu đã đến đích
        if current_node == end:
            path = []
            curr = current_node
            while curr in came_from:
                path.append(curr)
                curr = came_from[curr]
            path.append(start)
            path.reverse()
            return path, dist_total[end], time_total[end]

        # Duyệt các hàng xóm hợp lệ
        for edge in graph.get_neighbors(current_node, avoid_nodes, avoid_edges):
            neighbor = edge.destination
            
            # Trọng số tùy theo mode (Distance hoặc Time)
            weight = edge.distance if mode == 'distance' else edge.get_time(hour)
            tentative_g = g_score[current_node] + weight

            if neighbor not in g_score or tentative_g < g_score[neighbor]:
                came_from[neighbor] = current_node
                g_score[neighbor] = tentative_g
                dist_total[neighbor] = dist_total[current_node] + edge.distance
                time_total[neighbor] = time_total[current_node] + edge.get_time(hour)
                
                # Tính f(n) = g(n) + h(n)
                f_score = tentative_g + heuristic(graph, neighbor, end, mode)
                counter += 1
                pq.insert((f_score, counter, neighbor))

    return None, 0.0, 0.0