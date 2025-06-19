from collections import deque

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

def bfs_search(start, goal):
    queue = deque([[start]])
    visited = set()

    while queue:
        path = queue.popleft()  
        node = path[-1]         

        if node == goal:
            return path         

        elif node not in visited:
            for neighbor in graph[node]:
                new_path = list(path)
                new_path.append(neighbor)
                queue.append(new_path)

            visited.add(node)

    return None  

start_node = 'A'
goal_node = 'F'
result = bfs_search(start_node, goal_node)

if result:
    print(f"Jalur dari {start_node} ke {goal_node}: {' -> '.join(result)}")
else:
    print(f"Tidak ada jalur dari {start_node} ke {goal_node}.")
