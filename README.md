Smart Path Finder - RMIT Algorithms & Analysis 2026A
A high-performance, graph-based navigation system designed to compute optimal routes based on Shortest Distance and Fastest Travel Time. The system simulates real-world traffic patterns and supports dynamic avoidance of specific locations and roads.
👥 Team Members & Contributions
Below is the detailed contribution table for the project development phase:
Member
Student ID
Primary Role
Key Contributions
 
Tran Viet Hoang
[ID]
Infrastructure
Developed Core Graph data structures, Node/Edge classes, and Adjacency logic to handle large-scale datasets.
Nguyen Cong Phuong
[ID]
Query Engine
Implemented Query processing lifecycle, Input validation, and developed the terminal-based UI helpers for result formatting.
Nguyen Trong Nhan
[ID]
Algorithm Dev
Engineered the A* implementation for Shortest Distance using Euclidean Heuristics to optimize search space.
Duong Chan Phong
[ID]
Algorithm Dev
Developed the Time-Dependent A* logic for Fastest Time, incorporating dynamic 24-hour traffic profiles and congestion modeling.

Key Features
A* Search Optimization: High-speed pathfinding across thousands of nodes using geographically aware heuristics.
Time-Dependent Routing: Realistic travel time simulation with peak-hour multipliers (Morning / Evening Rush Hours).
Dynamic Avoidance: Real-time filtering of nodes and edges without requiring graph re-initialization.
Zero External Dependencies: Built strictly with Python Standard Library, featuring a custom-implemented Min-Heap.
Project Structure
.
├── main.py                 # Application entry point
├── Core/
│   ├── algorithm.py        # A* Pathfinding logic (Shortest & Fastest)
│   ├── graph.py            # Graph, Node, and Edge data structures
│   └── query.py            # Query lifecycle management and logic
├── Utility/
│   ├── heap.py             # Custom Min-Heap (No external libraries)
│   ├── data_loader.py      # Map generation and data loading
│   ├── input_helper.py     # Terminal user interaction helpers
│   └── display.py          # Result formatting UI
└── README.md               # Project documentation


Technical Analysis
1. Time Complexity
By utilizing a Min-Heap paired with an Adjacency List, the core algorithm operates at O((V + E) log V).
2. Space Complexity
The system maintains a memory footprint of O(V + E) for graph storage and search state management.
Demo Video
Watch our system demonstration here:
👉 [YOUR_YOUTUBE_LINK_HERE]
Appendix - AI Tools Usage
AI tools (Gemini/ChatGPT) were utilized for: Algorithm comparison, code refactoring for modularity, and documentation formatting. All business logic and implementations were verified and tested by the team.
