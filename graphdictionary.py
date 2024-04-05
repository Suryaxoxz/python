class Graph:
    def __init__(self):
        self.list = {}

    def add_ele(self, e, v):
        if e not in self.list:
            self.list[e] = [v]
        else:
            self.list[e] += [v]

        if v not in self.list:
            self.list[v] = [e]
        else:
            self.list[v] += [e]

    def print(self):
        for vertex, adj in self.list.items():
            print(vertex, "->", adj) 


g = Graph()

n = int(input())
print("Enter the edges (e v):")
for i in range(n):
    edge = input().split()
    e, v = int(edge[0]), int(edge[1])
    g.add_ele(e, v)

print("\nGraph:")
g.print()