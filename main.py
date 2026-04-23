"""
FILE: main.py
DESCRIPTION: Main entry point for the Smart Path Finder system.
"""

from Core.algorithm import a_star_distance
from Core.graph import Graph
# from Data.data_loader import load_map_data # To be implemented by teammates

def main():
    print("=== SMART PATH FINDER SYSTEM ===")

    # Initialize Graph
    city_map = Graph()

    # Define test parameters
    start_node = 0
    goal_node = 10
    
    print(f"\nSearching for shortest distance from Node {start_node} to Node {goal_node}...")
    
    # Execute Nhan's Algorithm
    path, distance = a_star_distance(
        city_map, 
        start_node, 
        goal_node, 
        avoid_nodes=[], 
        avoid_edges=[]
    )

    # Output Results
    if path:
        print("Success: Path found!")
        print(f"Route: {' -> '.join(map(str, path))}")
        print(f"Total Distance: {distance:.2f} units")
    else:
        print("Failure: No path found.")

if __name__ == "__main__":
    main()