import heapq
import networkx as nx
import matplotlib.pyplot as plt

class Graph:
    def __init__(self):
        self.graph = {}
        self.h = {}  # Heuristic values

    def add_edge(self, node1, node2, cost):
        if node1 not in self.graph:
            self.graph[node1] = []
        if node2 not in self.graph:
            self.graph[node2] = []
        self.graph[node1].append((node2, cost))
        self.graph[node2].append((node1, cost))  # Assuming an undirected graph

    def a_star_search(self, start, goal):
        open_list = []
        heapq.heappush(open_list, (0 + self.h[start], 0, start, []))  # (f, g, node, path)
        closed_set = set()
        
        while open_list:
            f, g, node, path = heapq.heappop(open_list)
            if node in closed_set:
                continue
            path = path + [node]
            
            if node == goal:
                return path, g  # Return path and cost
            
            closed_set.add(node)
            
            for neighbor, cost in self.graph.get(node, []):
                if neighbor not in closed_set:
                    heapq.heappush(open_list, (g + cost + self.h[neighbor], g + cost, neighbor, path))
        
        return None, float("inf")  # No path found

    def set_heuristic(self, h_values):
        self.h = h_values

def draw_graph(graph, path=None):
    G = nx.Graph()
    for node in graph.graph:
        for neighbor, cost in graph.graph[node]:
            G.add_edge(node, neighbor, weight=cost)
    
    pos = nx.spring_layout(G)
    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=2000, font_size=12)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
    
    if path:
        path_edges = [(path[i], path[i+1]) for i in range(len(path)-1)]
        nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color='r', width=2)
    
    plt.show()

# Example Usage
graph = Graph()
graph.add_edge('A', 'B', 4)
graph.add_edge('A', 'C', 3)
graph.add_edge('B', 'D', 5)
graph.add_edge('C', 'D', 6)
graph.add_edge('C', 'E', 7)
graph.add_edge('D', 'F', 2)
graph.add_edge('E', 'F', 4)
graph.add_edge('B', 'E', 8)
graph.add_edge('D', 'G', 3)
graph.add_edge('F', 'G', 1)

graph.set_heuristic({'A': 10, 'B': 8, 'C': 6, 'D': 4, 'E': 6, 'F': 2, 'G': 0})

start_node, goal_node = 'A', 'G'
path, cost = graph.a_star_search(start_node, goal_node)

if path:
    print(f"Shortest Path: {' -> '.join(path)} with Cost: {cost}")
    draw_graph(graph, path)
else:
    print("No path found")
