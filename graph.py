class Graph:
    def __init__(self,n):
        self.n = n
        self.d = {i:[] for i in range(n)}

    def add(self,u,v):
        if v not in self.d[u] and u not in self.d[v]:
            self.d[u].append(v)
            self.d[v].append(u)
        

    def remove(self,u,v):
        if v in self.d[u]:
            self.d[u].remove(v)
            self.d[v].remove(u)
        elif u in self.d[v]:
            self.d[v].remove(u)
            self.d[u].remove(v)


    def dft(self, start):
        visited = [False]*self.n
        self._dft(start,visited)

    def _dft(self, current, visited):
        if not visited[current]:
            print(current, end=' ')
            visited[current] = True
            for neighbor in sorted(self.d[current]):
                self._dft(neighbor, visited)

    def bft(self, start):
        visited = [False] * self.n
        queue = [start]
        visited[start] = True

        while queue:
            current = queue.pop(0)
            print(current, end=' ')
        
            for neighbor in sorted(self.d[current]):
                if not visited[neighbor]:
                    queue.append(neighbor)
                    visited[neighbor] = True


