import sys
import os
import time

# Ensure Python can find modules in core, utility, and data folders
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from core.graph import Graph
from core.algorithm import dijkstra
from data.data_loader import load_map_data

def main():
    # 1. INITIALIZATION AND DATA LOADING
    # Default path to the JSON data file
    data_file = os.path.join('data', 'map_data.json') 
    
    print("="*50)
    print("   SMART PATH FINDER SYSTEM - VERSION 2026A   ")
    print("="*50)
    print(f"[*] Loading map data from: {data_file}...")
    
    graph = load_map_data(data_file)
    
    if not graph.nodes:
        print("[!] Error: No data loaded. Please check data/map_data.json")
        return
    
    print(f"[+] Map loaded successfully with {len(graph.nodes)} locations.")
    print("-" * 50)

    # 2. QUERY SPECIFICATION (USER INPUT)
    try:
        # Input source and destination
        source = input(">> Enter Source Node: ").strip().upper()
        destination = input(">> Enter Destination Node: ").strip().upper()
        
        # Validate node existence
        if source not in graph.nodes or destination not in graph.nodes:
            print("[!] Error: One or both locations do not exist in the map.")
            return

        # Input departure hour
        hour_input = input(">> Enter Departure Hour (0-23): ").strip()
        hour = int(hour_input)
        if not (0 <= hour <= 23):
            print("[!] Error: Hour must be between 0 and 23.")
            return

        # Input nodes to avoid (Optional)
        avoid_n_input = input(">> Nodes to avoid (comma separated, or leave blank): ").strip().upper()
        avoid_nodes = set([n.strip() for n in avoid_n_input.split(',') if n.strip()])

        # Input edges to avoid (Optional) - Format: A-B, C-D
        avoid_e_input = input(">> Edges to avoid (e.g., A-B, B-C, or leave blank): ").strip().upper()
        avoid_edges = set()
        if avoid_e_input:
            for pair in avoid_e_input.split(','):
                nodes = pair.strip().split('-')
                if len(nodes) == 2:
                    # Sort tuple to ensure (A,B) and (B,A) are treated as the same edge
                    avoid_edges.add(tuple(sorted([nodes[0].strip(), nodes[1].strip()])))

    except ValueError:
        print("[!] Error: Invalid input format. Please check your entries.")
        return

    print("\n" + "*"*15 + " PROCESSING REQUEST " + "*"*15)

    # 3. ALGORITHM EXECUTION AND PERFORMANCE MEASUREMENT
    
    # Criterion 1: Shortest Distance
    start_d = time.time()
    path_dist, d_val, t_val = dijkstra(graph, source, destination, 'distance', hour, avoid_nodes, avoid_edges)
    runtime_d = (time.time() - start_d) * 1000 # Convert to milliseconds

    # Criterion 2: Fastest Travel Time
    start_t = time.time()
    path_time, d2_val, t2_val = dijkstra(graph, source, destination, 'time', hour, avoid_nodes, avoid_edges)
    runtime_t = (time.time() - start_t) * 1000

    # 4. OUTPUT REPORTING
    
    # Results for Distance Optimization
    print("\n[ RESULT 1: MINIMUM DISTANCE PATH ]")
    if path_dist:
        print(f" -> Sequence : {' -> '.join(path_dist)}")
        print(f" -> Distance : {d_val:.2f} units")
        print(f" -> Time     : {t_val:.2f} mins (at hour {hour})")
        print(f" -> Runtime  : {runtime_d:.4f} ms")
    else:
        print(" -> No path found with the given constraints.")

    # Results for Time Optimization
    print("\n[ RESULT 2: MINIMUM TRAVEL TIME PATH ]")
    if path_time:
        print(f" -> Sequence : {' -> '.join(path_time)}")
        print(f" -> Distance : {d2_val:.2f} units")
        print(f" -> Time     : {t2_val:.2f} mins (at hour {hour})")
        print(f" -> Runtime  : {runtime_t:.4f} ms")
    else:
        print(" -> No path found with the given constraints.")

    print("\n" + "="*50)
    print("            End of routing service            ")
    print("="*50)

if __name__ == "__main__":
    main()