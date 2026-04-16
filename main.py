import json
import os
import time
from core.algorithms import SmartPathFinder
from utils.exporters import export_kml

def main():
    os.system('clear')
    print("=== RMIT SMART PATH FINDER (HD EDITION) ===")
    
    # Nạp dữ liệu
    with open('data/map_data.json', 'r') as f:
        data = json.load(f)
    nodes, edges = data['nodes'], data['edges']
    graph = {node: [] for node in nodes}
    for edge in edges: graph[edge['from']].append(edge)

    finder = SmartPathFinder(graph, nodes)

    # Nhập Input
    start = input("📍 Start Node ID: ")
    end = input("🏁 End Node ID: ")
    hour = int(input("⏰ Start Hour (0-23): "))
    
    avoid_n_raw = input("🚫 Avoid Nodes (ID1, ID2...): ")
    avoid_n = [x.strip() for x in avoid_n_raw.split(',')] if avoid_n_raw else []
    
    # --- PHẦN SỬA LỖI TRONG main.py ---
    avoid_e_raw = input("🚫 Avoid Edges (ID1-ID2, ID3-ID4...): ")
    avoid_e = []
    if avoid_e_raw:
        pairs = avoid_e_raw.split(',')
        for pair in pairs:
            if '-' in pair:
                try:
                    u, v = pair.strip().split('-')
                    avoid_e.append((u, v))
                except ValueError:
                    print(f"⚠️ Cảnh báo: Định dạng cạnh '{pair}' không đúng, sẽ bị bỏ qua.")
            else:
                print(f"⚠️ Cảnh báo: Cạnh '{pair}' thiếu dấu '-', sẽ bị bỏ qua.")
    
    # Chạy 2 tiêu chí theo đề bài
    res = [
        ("KHOẢNG CÁCH NGẮN NHẤT", finder.find_path(start, end, hour, 'dist', avoid_n, avoid_e)),
        ("THỜI GIAN NHANH NHẤT", finder.find_path(start, end, hour, 'time', avoid_n, avoid_e))
    ]

    for label, (path, d, t) in res:
        print(f"\n>>> {label}")
        if path:
            print(f"Lộ trình: {' -> '.join(path)}")
            print(f"Tổng: {round(d, 2)} km | {round(t, 1)} phút")
            export_kml(path, nodes, f"{label.replace(' ', '_')}.kml")
        else:
            print("Không tìm thấy đường đi thỏa mãn điều kiện.")

if __name__ == "__main__":
    main()