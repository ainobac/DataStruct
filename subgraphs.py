class Graph:
    def __init__(self,n):
        self.n = n
        self.sub = [[] for _ in range(n)]
        self.visited = [False]*n

    def add(self,u,v):
        self.sub[u].append(v)
        self.sub[v].append(u)

    def remove(self,u,v):
        if self.sub[u] and v in self.sub[u]:
            self.sub[u].remove(v)
        if self.sub[v] and u in self.sub[v]:
            self.sub[v].remove(u)

    def dfs(self,node):
        if not self.visited[node]:
            self.visited[node] = True
            for neighb in self.sub[node]:
                self.dfs(neighb)
    
    def subgraphs(self):
        count = 0
        self.visited = [False]*self.n
        for node in range(self.n):
            if not self.visited[node]:
                count += 1
                self.dfs(node)
        return count
    