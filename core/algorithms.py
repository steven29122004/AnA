import math
from core.base import Pathfinder
from utils.heap import MinHeap

class SmartPathFinder(Pathfinder):
    def heuristic(self, u, v):
        # Khoảng cách chim bay giữa 2 tọa độ (Euclidean distance)
        node_u = self.nodes[u]
        node_v = self.nodes[v]
        return math.sqrt((node_u['x'] - node_v['x'])**2 + (node_u['y'] - node_v['y'])**2)

    def find_path(self, start, end, start_hour, mode='time', avoid_nodes=None, avoid_edges=None):
        avoid_nodes = avoid_nodes or []
        avoid_edges = avoid_edges or []
        
        # g_score: chi phí thực tế từ điểm bắt đầu
        g_score = {node: float('inf') for node in self.nodes}
        g_score[start] = 0
        
        predecessors = {node: None for node in self.nodes}
        track_dist = {node: 0 for node in self.nodes}
        track_time = {node: 0 for node in self.nodes}

        pq = MinHeap()
        # (f_score, node_id) -> f(n) = g(n) + h(n)
        pq.push((0 + self.heuristic(start, end), start))

        while len(pq.heap) > 0:
            _, u = pq.pop()

            if u == end: break

            for edge in self.graph.get(u, []):
                v = edge['to']
                
                # 1. Check Avoidance
                if v in avoid_nodes: continue
                if (u, v) in avoid_edges or (v, u) in avoid_edges: continue

                # 2. Dynamic Time Logic: Tính giờ dựa trên thời gian đã trôi qua
                # Giả sử travel_time đơn vị là phút, quy đổi ra giờ để lấy index 0-23
                elapsed_hours = int(track_time[u] // 60)
                current_hour = (start_hour + elapsed_hours) % 24
                
                d = edge['dist']
                t = edge['times'][current_hour]
                
                weight = d if mode == 'dist' else t
                new_g_score = g_score[u] + weight

                if new_g_score < g_score[v]:
                    g_score[v] = new_g_score
                    track_dist[v] = track_dist[u] + d
                    track_time[v] = track_time[u] + t
                    predecessors[v] = u
                    
                    # f(n) = g(n) + heuristic (khoảng cách còn lại tới đích)
                    f_score = new_g_score + self.heuristic(v, end)
                    pq.push((f_score, v))

        path = []
        curr = end
        while curr is not None:
            path.append(curr)
            curr = predecessors[curr]
        
        if not path or path[-1] != start: return None, 0, 0
        return path[::-1], track_dist[end], track_time[end]