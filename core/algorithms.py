from core.base import Pathfinder
from utils.heap import MinHeap

class DijkstraFinder(Pathfinder):
    def find_path(self, start, end, hour, mode='time'):
        distances = {node: float('inf') for node in self.nodes}
        distances[start] = 0
        predecessors = {node: None for node in self.nodes}
        
        pq = MinHeap()
        pq.push((0, start))

        while len(pq.heap) > 0:
            current_cost, u = pq.pop()

            if u == end: break
            if current_cost > distances[u]: continue

            for edge in self.graph.get(u, []):
                v = edge['to']
                # Chế độ 'dist' lấy khoảng cách cố định, 'time' lấy theo khung giờ
                weight = edge['dist'] if mode == 'dist' else edge['times'][hour]
                new_dist = current_cost + weight
                
                if new_dist < distances[v]:
                    distances[v] = new_dist
                    predecessors[v] = u
                    pq.push((new_dist, v))

        path = []
        curr = end
        while curr:
            path.append(curr)
            curr = predecessors[curr]
        return path[::-1], distances[end]