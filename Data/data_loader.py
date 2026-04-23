import json
import os
from core.graph import Graph

def load_map_data(file_path):
    """
    Đọc dữ liệu từ file JSON và nạp vào đối tượng Graph.
    """
    graph = Graph()
    
    if not os.path.exists(file_path):
        print(f"Error: File {file_path} not found.")
        return graph

    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f) # Đọc toàn bộ file JSON thành list
            
            for edge in data:
                u = str(edge['u']).strip().upper()
                v = str(edge['v']).strip().upper()
                dist = float(edge['distance'])
                time_list = edge['time_list']
                
                # Nạp vào đồ thị
                graph.add_edge(u, v, dist, time_list)
                
    except Exception as e:
        print(f"Error parsing JSON: {e}")
            
    return graph