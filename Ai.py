from collections import deque

# Representasi graf menggunakan dictionary
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

def bfs_search(start, goal):
    # Antrian untuk BFS
    queue = deque([[start]])
    visited = set()

    while queue:
        path = queue.popleft()  # Ambil jalur dari depan antrian
        node = path[-1]         # Ambil node terakhir dari jalur

        if node == goal:
            return path         # Jika goal ditemukan, kembalikan jalur

        elif node not in visited:
            for neighbor in graph[node]:
                new_path = list(path)
                new_path.append(neighbor)
                queue.append(new_path)

            visited.add(node)

    return None  # Jika tidak ditemukan jalur

# Contoh penggunaan
start_node = 'A'
goal_node = 'F'
result = bfs_search(start_node, goal_node)

if result:
    print(f"Jalur dari {start_node} ke {goal_node}: {' -> '.join(result)}")
else:
    print(f"Tidak ada jalur dari {start_node} ke {goal_node}.")
