import random
from core.graph import Graph

def generate_map():
    """
    Tạo đồ thị ít nhất 1000 nodes theo dạng mạng lưới đường phố (Grid Network).
    Size: 32x32 = 1024 nodes.
    """
    graph = Graph()
    grid_size = 32 
    
    print(f"[*] Generating realistic road network ({grid_size}x{grid_size} nodes)...")

    # 1. Tạo Nodes với tọa độ X, Y
    for x in range(grid_size):
        for y in range(grid_size):
            node_id = f"N_{x}_{y}"
            # Mỗi block cách nhau 2.5 km
            graph.add_node(node_id, x * 2.5, y * 2.5)

    # 2. Tạo Edges (Đường đi nối các block liền kề)
    for x in range(grid_size):
        for y in range(grid_size):
            u = f"N_{x}_{y}"
            
            # Chỉ nối sang phải và xuống dưới để tránh trùng lặp 
            # (Hàm add_edge trong graph.py đã lo việc nối 2 chiều)
            neighbors = []
            if x < grid_size - 1: neighbors.append(f"N_{x+1}_{y}")
            if y < grid_size - 1: neighbors.append(f"N_{x}_{y+1}")

            for v in neighbors:
                # 15% khả năng bị chặn (không có đường nối)
                # if random.random() < 0.15:
                    # continue
                    
                # Khoảng cách dao động từ 2.0 đến 3.5 km
                distance = random.uniform(2.0, 3.5)
                
                # Tạo 24 mốc thời gian. Giả sử ban đêm (0-5h) kẹt xe ít, ban ngày (6-20h) kẹt nhiều
                times = []
                for hour in range(24):
                    if 6 <= hour <= 20:
                        times.append(random.uniform(5.0, 15.0)) # Phút
                    else:
                        times.append(random.uniform(2.5, 6.0))  # Phút
                
                graph.add_edge(u, v, distance, times)

    return graph