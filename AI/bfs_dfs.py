from collections import deque

# Define the graph as an adjacency list
graph = {
    'A': ['B', 'D'],
    'B': ['C', 'F'],
    'C': ['E', 'G'],
    'D': [],
    'E': ['B', 'F'],
    'F': ['A'],
    'G': ['E']
}

def bfs(graph, start, goal):
    # Initialize the queues
    Q1 = deque([start])  # Queue of nodes to be processed
    Q2 = []  # Queue of processed nodes
    parent_map = {start: None}  # Dictionary to store the parent of each node
    
    while Q1:
        # Dequeue a node from Q1
        current_node = Q1.popleft()
        
        # If goal node is found, reconstruct the path
        if current_node == goal:
            path = []
            while current_node is not None:
                path.append(current_node)
                current_node = parent_map[current_node]
            return path[::-1]  # Reverse the path to get the correct order
        
        # Process the current node and add its neighbors to Q1
        Q2.append(current_node)  # Mark the node as processed
        for neighbor in graph[current_node]:
            if neighbor not in Q2 and neighbor not in Q1:  # Only add unvisited neighbors
                Q1.append(neighbor)
                parent_map[neighbor] = current_node  # Set the parent of the neighbor
    
    return None  # Return None if no path is found

# Define the start and goal nodes
start_node = 'A'
goal_node = 'E'

# Call BFS to find the path
path = bfs(graph, start_node, goal_node)

if path:
    print(f"Path from {start_node} to {goal_node}: {' -> '.join(path)}")
else:
    print(f"No path found from {start_node} to {goal_node}")
