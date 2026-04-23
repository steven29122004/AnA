import sys
import os
import time

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from data.data_loader import generate_map
from core.algorithm import a_star

def main():
    print("="*50)
    print("   SMART PATH FINDER (A* ALGORITHM)   ")
    print("="*50)
    
    # Gọi hàm gen data của leader yêu cầu
    graph = generate_map()
    print(f"[+] Successfully generated {len(graph._nodes)} nodes.")
    print("-" * 50)

    try:
        # Nhập liệu
        source = input(">> Enter Source Node (e.g., N_0_0): ").strip()
        destination = input(">> Enter Destination Node (e.g., N_31_31): ").strip()
        
        if not graph.has_node(source) or not graph.has_node(destination):
            print("[!] Error: Node does not exist in the map.")
            return

        hour = int(input(">> Enter Departure Hour (0-23): "))
        if not (0 <= hour <= 23):
            print("[!] Error: Hour must be between 0 and 23.")
            return

        # Avoid Nodes & Edges (Để trống nếu không cấm)
        avoid_n_input = input(">> Nodes to avoid (comma separated): ").strip()
        avoid_nodes = set([n.strip() for n in avoid_n_input.split(',') if n.strip()])

        avoid_e_input = input(">> Edges to avoid (e.g., N_0_0-N_0_1): ").strip()
        avoid_edges = set()
        if avoid_e_input:
            for pair in avoid_e_input.split(','):
                nodes = pair.strip().split('-')
                if len(nodes) == 2:
                    avoid_edges.add(tuple(sorted([nodes[0].strip(), nodes[1].strip()])))

    except ValueError:
        print("[!] Error: Invalid input.")
        return

    print("\n" + "*"*15 + " CALCULATING WITH A* " + "*"*15)

    # Tối ưu khoảng cách
    start_time = time.time()
    path_d, dist1, time1 = a_star(graph, source, destination, 'distance', hour, avoid_nodes, avoid_edges)
    run_d = (time.time() - start_time) * 1000

    # Tối ưu thời gian
    start_time = time.time()
    path_t, dist2, time2 = a_star(graph, source, destination, 'time', hour, avoid_nodes, avoid_edges)
    run_t = (time.time() - start_time) * 1000

    # In kết quả
    print("\n[ RESULT 1: SHORTEST PATH (DISTANCE) ]")
    if path_d:
        # In 5 node đầu và 5 node cuối cho gọn nếu đường quá dài
        path_str = " -> ".join(path_d) if len(path_d) <= 10 else f"{' -> '.join(path_d[:5])} ... -> {' -> '.join(path_d[-5:])}"
        print(f" -> Path     : {path_str} (Total: {len(path_d)} nodes)")
        print(f" -> Distance : {dist1:.2f} km")
        print(f" -> Runtime  : {run_d:.2f} ms")
    else:
        print(" -> No path found.")

    print("\n[ RESULT 2: FASTEST PATH (TIME) ]")
    if path_t:
        path_str = " -> ".join(path_t) if len(path_t) <= 10 else f"{' -> '.join(path_t[:5])} ... -> {' -> '.join(path_t[-5:])}"
        print(f" -> Path     : {path_str} (Total: {len(path_t)} nodes)")
        print(f" -> Time     : {time2:.2f} mins")
        print(f" -> Runtime  : {run_t:.2f} ms")
    else:
        print(" -> No path found.")

    print("\n" + "="*50)

if __name__ == "__main__":
    main()