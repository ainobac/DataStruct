class HashLinear:
    def __init__(self, M):
        self.M = M
        self.T = [None]*M

    def hash_c(self, data):
        sum = 0
        for c in data:
            sum += ord(c)
        return sum%self.M
    
    def insert(self, data):
        if all(x is not None for x in self.T):
            return
    
        i = self.hash_c(data)
        while self.T[i] is not None:
            if self.T[i] == data:
                return
            i = (i+1)%self.M
        self.T[i] = data

    def delete(self, data):
        i = self.hash_c(data)
        if self.T[i] == data:
            self.T[i] = None
        else:
            ind = 0
            while ind < self.M:
                if self.T[ind] == data:
                    self.T[ind] = None
                    break
                ind += 1

    def print(self):
        for x in self.T:
            if x is not None:
                print(x, end=" ")
