#A*
import heapq

def a_star(start, goal, graph, heuristic):
    frontier = []
    heapq.heappush(frontier, (0, start))
    came_from = {}
    cost_so_far = {}
    came_from[start] = None
    cost_so_far[start] = 0
    
    while frontier:
        current = heapq.heappop(frontier)[1]
        
        if current == goal:
            break
        
        for next in graph[current]:
            new_cost = cost_so_far[current] + graph[current][next]
            if next not in cost_so_far or new_cost < cost_so_far[next]:
                cost_so_far[next] = new_cost
                priority = new_cost + heuristic(goal, next)
                heapq.heappush(frontier, (priority, next))
                came_from[next] = current
    
    path = []
    current = goal
    while current != start:
        path.append(current)
        current = came_from[current]
    path.append(start)
    path.reverse()
    return path

# Example Usage
graph = {
    'A': {'B': 5, 'C': 10, 'D': 8},
    'B': {'E': 6},
    'C': {'E': 3, 'F': 2},
    'D': {'F': 7},
    'E': {'G': 6},
    'F': {'G': 3},
    'G': {}
}

heuristic = lambda a, b: abs(ord(a) - ord(b))

start = str(input("Enter Start state: ")) #A
goal = str(input("Enter Goal state: "))   #G

path = a_star(start, goal, graph, heuristic)

print(path)  # Output: ['A', 'C', 'F', 'G']
