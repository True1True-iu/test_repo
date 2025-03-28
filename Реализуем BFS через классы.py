from collections import deque

class Node:
    def __init__(self, value):
        self.value = value

        self.outbound = []
        self.inbound = []

    def point_to(self, other):
        self.outbound.append(other)
        other.inbound.append(self)

    def __str__(self):
        return f'Node({self.value})'

class Graph:
    def __init__(self, root):
        self._root = root

    def dfs(self, vertex, visited):
        if vertex not in visited:
            print(vertex, end=' ')
            visited.append(vertex)
            for neighbor in vertex.outbound:
                self.dfs(neighbor, visited)

    def bfs(self):
        visited = []
        queue = deque([self._root])

        while queue:
            vertex = queue.popleft()
            if vertex not in visited:
                print(vertex, end=' ')
                visited.append(vertex)
                for neighbor in vertex.outbound:
                    queue.append(neighbor)

a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
a.point_to(b)
b.point_to(c)
c.point_to(d)
d.point_to(a)
b.point_to(d)

g = Graph(a)

visited = []
g.dfs(a, visited)
g.bfs()