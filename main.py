# File chạy chính (Giao diện Console/Menu)
import json
from core.algorithms import dijkstra
from utils.exporters import export_kml

def main():
    # 1. Đọc dữ liệu từ file JSON
    with open('data/map_data.json', 'r') as f:
        data = json.load(f)
    
    nodes = data['nodes']
    # Biến list edges thành dictionary để thuật toán chạy nhanh hơn
    graph = {node: [] for node in nodes}
    for edge in data['edges']:
        graph[edge['from']].append(edge)

    # 2. Input từ người dùng (Steven nhập thử)
    start = "A"
    end = "D"
    hour = 17 # 5h chiều

    # 3. Chạy thuật toán
    path, cost = dijkstra(nodes, graph, start, end, hour, mode='time')

    # 4. Show kết quả
    if path:
        print(f"Lộ trình từ {start} đến {end}: {' -> '.join(path)}")
        print(f"Tổng chi phí: {cost}")
        export_kml(path, nodes, "Steven_Result.kml")

if __name__ == "__main__":
    main()