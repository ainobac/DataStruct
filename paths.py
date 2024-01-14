
class Graph:
    def __init__(self,n):
        self.n = n
        self.matrix = [[float('inf') for _ in range(n)] for _ in range(n)]
        for i in range(n):
            self.matrix[i][i] = 0

    def add(self,u,v,w):
        if 0 <= u < self.n and 0 <= v < self.n:
            self.matrix[u][v] = w

    def remove(self,u,v):
        self.matrix[u][v] = float('inf')

    def all_paths(self):
        matrix = [row[:] for row in self.matrix]

        for k in range(self.n):
            for i in range(self.n):
                for j in range(self.n):
                    if matrix[i][k] + matrix[k][j] < matrix[i][j]:
                        matrix[i][j] = matrix[i][k] + matrix[k][j]

        for i in range(self.n):
            for j in range(self.n):
                if matrix[i][j] == float('inf'):
                    matrix[i][j] = -1
        
        return matrix


