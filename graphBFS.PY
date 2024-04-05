class adj_node:
    def __init__(self, vertex, value):
        self.vertex = vertex
        self.value = value
        self.next = None

class graph:
    def __init__(self, n):
        self.n = n
        self.graph = [None] * n

    def add_ele(self, src, dest, value):
        node = adj_node(dest, value)
        node.next = self.graph[src]
        self.graph[src] = node

        node = adj_node(src, value)
        node.next = self.graph[dest]
        self.graph[dest] = node

def print(graph):
    for i, n in enumerate(graph.graph):
        linked_list = []
        while n is not None:
            linked_list.append(str(n.vertex))
            n = n.next
        print(f'Node {i} -> '+' -> '.join(linked_list))

def BFS(graph):
    visited_ele={}
    queue_ele=[]
    for i in graph:
        print(i)


g = graph(5)
g.add_ele(0, 1, 4)
g.add_ele(0, 4, 1)
g.add_ele(1, 4, 4)
g.add_ele(1, 3, 1)
g.add_ele(1, 2, 2)
g.add_ele(3, 4, 1)
g.add_ele(2, 3, 3)

print(g)
BFS(g)
