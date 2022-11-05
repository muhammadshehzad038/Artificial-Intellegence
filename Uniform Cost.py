import math


def findMin(frontier):
    minX = math.inf
    node = ""
    for i in frontier:
        if minX > frontier[i][1]:
            minX = frontier[i][1]
            node = i
        return node


class Node:
    def __init__(self, state, parent, actions, totalCost):
        self.state = state
        self.parent = parent
        self.actions = actions
        self.totalCost = totalCost


def actionSequence(graph, initialState, goalState):
    solution = goalState
    currentparent = graph[goalState].parent
    while currentparent != 0:
        solution.append(currentparent)
        currentparent = graph[currentparent].parent
    solution.reverse()
    return solution


def UCS():
    initialSate = 'C'
    goalState = 'D'
    graph = {'A': Node('A', None, [('B', 6), ('C', 9), ('E', 1)], 0),
             'B': Node('B', None, [('A', 6), ('D', 9), ('E', 4)], 0),
             'C': Node('C', None, [('A', 6), ('F', 9), ('E', 3)], 0),
             'D': Node('D', None, [('B', 6), ('E', 9), ('E', 7)], 0),
             'E': Node('E', None, [('A', 1), ('B', 4), ('D', 5), ('D', 5), ('F', 6)], 0),
             'F': Node('F', None, [('C', 2), ('E', 6), ('D', 7)], 0),
             'G': Node('G', None, [('C', 3)], 0)}

    frontier = dict()
    frontier[initialSate] = (None, 0)
    explored = []

    while len(frontier) != 0:
        currentNode = findMin(frontier)
        del frontier[currentNode]
        if graph[currentNode].state == goalState:
            return actionSequence(graph, initialSate, goalState)
        explored.append(currentNode)
        for child in graph[currentNode].actions:
            currentCost = child[1] + graph[currentNode].totalCost
            if child[0] not in frontier and child[0] not in explored:
                graph[child[0]].parent = currentNode
                graph[child[0]].totalCost = currentCost
                frontier[child[0]] = (graph[child[0]].parent, graph[child[0]].totalCost)
            elif child[0] in frontier:
                if frontier[child[0][1]] < currentCost:
                    graph[child[0]].parent = frontier[child[0]][0]
                    graph[child[0]].totalCost = frontier[child[0]][1]
                else:
                    frontier[child[0]] = (currentNode, currentCost)
                    graph[child[0]].parent = frontier[child[0]][0]
                    graph[child[0]].totalCost = frontier[child[0]][1]


print(UCS())
