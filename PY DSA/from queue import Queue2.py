from queue import Queue
graph_adj_lst = {
    'A' : ['B', 'D'],
    'B' : ['C', 'F'],
    'C' : ['E', 'G', 'H'],
    'G' : ['E', 'H'],
    'E' : ['B', 'F'],
    'F' : ['A'],
    'D' : ['F'],
    'H' : ['A'],
}
"""
graph_adj_lst = {
    'M' : ['N', 'Q', 'R'],
    'N' : ['O', 'Q', 'M'],
    'R' : ['M'],
    'O' : ['P', 'N'],
    'Q' : ['M', 'N'],
    'P' : ['O', 'Q'],
}
"""
visited = {}
level = {}
parent = {}
bfs_traversal = []
queue = Queue()
for node in graph_adj_lst:
    visited[node] = False
    parent[node] = None
    level[node] = -1
print(visited)
print(level)
print(parent)
# source = 'A' -> source = 'C'
source = 'H'
visited[source] = True
level[source] = 0
queue.put(source)
while not queue.empty():
    u = queue.get()
    bfs_traversal.append(u)
    for v in graph_adj_lst[u]:
        if not visited[v]:
            visited[v] = True
            parent[v] = u
            print(parent[v])
            level[v] = level[u] + 1
            queue.put(v)
print("BFS traversal : ", bfs_traversal)
# print(level['N'])
# print(level['O'])
# src_node = 'H' -> dest_node = 'D'
node = 'D' # source node
path = []
while node is not None:
    path.append(node)
    node = parent[node]
path.reverse()
print("shortest path is : ", path)