import json
import os
from core.algorithms import DijkstraFinder
from utils.exporters import export_kml

def main():
    # Load data
    with open('data/map_data.json', 'r') as f:
        data = json.load(f)
    
    nodes = data['nodes']
    graph = {node: [] for node in nodes}
    for edge in data['edges']:
        graph[edge['from']].append(edge)

    # Init & Run
    finder = DijkstraFinder(graph, nodes)
    
    start_node = "A"
    end_node = "D"
    current_hour = 17 # 5h chiều (giờ cao điểm)

    path, cost = finder.find_path(start_node, end_node, current_hour, mode='time')

    if path:
        print(f"✅ Thành công! Lộ trình: {' -> '.join(path)}")
        print(f"⏱️ Tổng thời gian (lúc {current_hour}h): {cost} phút")
        export_kml(path, nodes, "Steven_Result.kml")
    else:
        print("❌ Không tìm thấy đường đi!")

if __name__ == "__main__":
    main()