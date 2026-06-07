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
    """
    'M' : ['N', 'Q', 'R'],
    'N' : ['O', 'Q', 'M'],
    'R' : ['M'],
    'O' : ['P', 'N'],
    'Q' : ['M', 'N'],
    'P' : ['O', 'Q'],
    """
}
def dfs(graph, src_node, seen, dest_node):
    if src_node not in seen:
        seen.append(src_node)
        for i in graph[src_node]:
            if seen[-1] is dest_node:
                break
            dfs(graph, i, seen, dest_node)
        return seen
print(dfs(graph_adj_lst, 'A', [], 'H'))
# print(dfs(graph_adj_lst, 'M', [], 'R'))