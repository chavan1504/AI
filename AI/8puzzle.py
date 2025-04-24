import heapq
import networkx as nx
import matplotlib.pyplot as plt

# Define the given initial and goal states
INITIAL_STATE = [[1, 2, 3], [4, 0, 6], [7, 5, 8]]
GOAL_STATE = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
MOVES = {"UP": (-1, 0), "DOWN": (1, 0), "LEFT": (0, -1), "RIGHT": (0, 1)}

def manhattan_distance(state):
    distance = 0
    for i in range(3):
        for j in range(3):
            value = state[i][j]
            if value != 0:
                goal_x, goal_y = [(row, col) for row in range(3) for col in range(3) if GOAL_STATE[row][col] == value][0]
                distance += abs(goal_x - i) + abs(goal_y - j)
    return distance

def find_blank(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j
    return None

def generate_new_state(state, move):
    x, y = find_blank(state)
    dx, dy = MOVES[move]
    new_x, new_y = x + dx, y + dy
    if 0 <= new_x < 3 and 0 <= new_y < 3:
        new_state = [row[:] for row in state]
        new_state[x][y], new_state[new_x][new_y] = new_state[new_x][new_y], new_state[x][y]
        return new_state
    return None

def state_to_tuple(state):
    return tuple(tuple(row) for row in state)

def is_solvable(state):
    flat_list = [num for row in state for num in row if num != 0]
    inversions = sum(1 for i in range(len(flat_list)) for j in range(i + 1, len(flat_list)) if flat_list[i] > flat_list[j])
    return inversions % 2 == 0

def a_star_search(initial_state):
    if not is_solvable(initial_state):
        print("Given initial state is unsolvable!")
        return None, None

    open_list = []
    heapq.heappush(open_list, (manhattan_distance(initial_state), 0, initial_state, []))
    visited = set()
    parent_map = {}

    while open_list:
        _, cost, current_state, path = heapq.heappop(open_list)

        if current_state == GOAL_STATE:
            return path + [current_state], parent_map

        visited.add(state_to_tuple(current_state))

        for move in MOVES.keys():
            new_state = generate_new_state(current_state, move)
            if new_state and state_to_tuple(new_state) not in visited:
                new_cost = cost + 1
                heapq.heappush(open_list, (new_cost + manhattan_distance(new_state), new_cost, new_state, path + [new_state]))
                parent_map[state_to_tuple(new_state)] = state_to_tuple(current_state)

    return None, None

def visualize_tree_with_f_values(initial_state, solution_path, parent_map, max_depth=6):
    G = nx.DiGraph()
    pos = {}
    f_values = {}

    queue = [(state_to_tuple(initial_state), (0, 0), 0, 0)]
    pos[state_to_tuple(initial_state)] = (0, 0)
    f_values[state_to_tuple(initial_state)] = manhattan_distance(initial_state)

    while queue:
        node, position, depth, f_value = queue.pop(0)
        if depth >= max_depth:
            continue

        children = [child for child, parent in parent_map.items() if parent == node]
        num_children = len(children)
        start_x = position[0] - num_children / 2
        y = position[1] - 1

        for i, child in enumerate(children):
            child_state = tuple(map(tuple, child))
            g_value = solution_path.index(child) if child in solution_path else depth + 1
            h_value = manhattan_distance(child)
            f_value = g_value + h_value
            f_values[child_state] = f_value

            child_pos = (start_x + i, y)
            pos[child_state] = child_pos
            queue.append((child, child_pos, depth + 1, f_value))
            G.add_edge(node, child_state)

    plt.figure(figsize=(12, 8))
    nx.draw(G, pos, with_labels=False, node_size=500, node_color="green", edge_color="black")

    for node, (x, y) in pos.items():
        matrix_str = "\n".join([" ".join(map(str, row)) for row in node])
        f_text = f"f={f_values[node]}"
        plt.text(x, y, matrix_str, fontsize=8, ha="center", va="center", color="white",
                 bbox=dict(facecolor="green", edgecolor="black", boxstyle="round,pad=0.3"))
        plt.text(x, y - 0.2, f_text, fontsize=8, ha="center", va="center", color="red")

    plt.show()

# Run the search and visualization
solution_path, parent_map = a_star_search(INITIAL_STATE)
if solution_path:
    visualize_tree_with_f_values(INITIAL_STATE, solution_path, parent_map, max_depth=6)
else:
    print("No solution found")
