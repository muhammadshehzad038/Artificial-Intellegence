# Node Class
class Node:
    def __init__(self, node_state, node_parent, node_actions, node_cost):
        self.state = node_state
        self.parent = node_parent
        self.actions = node_actions
        self.cost = node_cost


# Helper function for generating path sequence and path cost from graph
# by BFS

def generate_sequence(goal_state):
    path_cost = 0
    solution = [goal_state]
    states_parent = graph[goal_state].parent
    prev_node = goal_state
    while states_parent is not None:
        for i in range(len(graph[states_parent].actions)):
            if graph[states_parent].actions[i] == prev_node:
                path_cost += (graph[states_parent].cost[i])
                solution.append(states_parent)
                prev_node = states_parent
                states_parent = graph[states_parent].parent
                solution.reverse()
            return solution, path_cost


# Breadth first algorithm function
def BFS(initial_state, goal):
    goal_state = goal
    solution = []
    current_states = [initial_state]
    explored = []
    found = False
    while len(current_states) != 0:
        current_state = current_states[0]
        explored.append(current_states.pop(0))
        for child in graph[current_state].actions:
            if child not in explored and child not in current_states:
                current_states.append(child)
                graph[child].parent = current_state
                if child == goal_state:
                    found = True
                    solution = generate_sequence(goal_state)
                    break
        if found:
            return solution


# graph provided to algorithm
graph = {
    'A': Node('A', None, ['B'], [1]),
    'B': Node('B', None, ['A', 'C'], [1, 1]),
    'C': Node('C', None, ['B', 'D'], [1, 1]),
    'D': Node('D', None, ['C', 'Y', 'E'], [1, 1, 1]),
    'E': Node('E', None, ['D', 'F'], [1, 1]),
    'F': Node('F', None, ['E', 'G'], [1, 1]),
    'G': Node('G', None, ['F', 'H'], [1, 1]),
    'H': Node('H', None, ['G', 'I'], [1, 1]),
    'I': Node('I', None, ['H', 'J'], [1, 1]),
    'J': Node('J', None, ['I', 'K'], [1, 1]),
    'K': Node('K', None, ['J', 'L'], [1, 1]),
    'L': Node('L', None, ['K', 'M'], [1, 1]),
    'M': Node('M', None, ['L', 'N'], [1, 1]),
    'N': Node('N', None, ['M', 'O'], [1, 1]),
    'O': Node('O', None, ['N', 'P', 'Z'], [1, 1, 1]),
    'P': Node('P', None, ['O', 'Q'], [1, 1]),
    'Q': Node('Q', None, ['P', 'R'], [1, 1]),
    'R': Node('R', None, ['Q', 'S', 'T'], [1, 1, 1]),
    'S': Node('S', None, ['R'], [1]),
    'T': Node('T', None, ['R', 'U'], [1, 1]),
    'U': Node('U', None, ['T', 'V', 'W'], [1, 1, 1]),
    'V': Node('V', None, ['U', 'X'], [1, 1]),
    'W': Node('W', None, ['U', 'X'], [1, 1]),
    'X': Node('X', None, ['W', 'V', 'Y'], [1, 1]),
    'Y': Node('Y', None, ['X', 'D'], [1, 1]),
    'Z': Node('Z', None, ['O'], [1])
}
# Note: cities can be changes in BFS call
path = BFS("A", "Z")
print("Path: " + str(path[0]))
print("Path Cost: " + str(path[1]))
