import networkx as nx
import matplotlib.pyplot as plt
from collections import deque

# --- Search Functions ---
def bfs(graph, start):
    visited = []
    queue = deque([start])
    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.append(node)
            for neighbor in graph.get(node, []):
                if neighbor not in visited:
                    queue.append(neighbor)
    return visited

def dfs(graph, start, visited=None):
    if visited is None:
        visited = []
    visited.append(start)
    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)
    return visited

def iddfs(graph, start, max_depth):
    def dls(node, depth, visited):
        if depth == 0:
            return [node]
        result = [node]
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                result.extend(dls(neighbor, depth - 1, visited))
        return result

    for depth in range(max_depth + 1):
        visited = set()
        result = dls(start, depth, visited)
        if len(result) == len(graph):
            return result
    return result

# --- Graph Definition ---
graph = {
    'A': ['B', 'C', 'D'],
    'B': [],
    'C': ['E'],
    'D': ['F'],
    'E': [],
    'F': ['G'],
    'G': []
}

# --- Visualization ---
G = nx.DiGraph()
for node, neighbors in graph.items():
    for neighbor in neighbors:
        G.add_edge(node, neighbor)

plt.figure(figsize=(6, 5))
pos = nx.spring_layout(G)  # auto layout
nx.draw(
    G, pos,
    with_labels=True,
    node_color='lightblue',
    node_size=2000,
    font_size=12,
    font_weight='bold',
    arrows=True
)
plt.title("Graph Representation")
plt.show()

# --- Run Searches ---
print("BFS:", bfs(graph, 'A'))
print("DFS:", dfs(graph, 'A'))
print("IDDFS:", iddfs(graph, 'A', max_depth=3))
