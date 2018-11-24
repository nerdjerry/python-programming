class unionFind(object):
    def __init__(self):
        self.id = [0,1,2,3,4,5,6,7,8,9]
        self.size = [1] * 10

    def root(self,node):
        if self.id[node]!= node:
            self.id[node] = self.root(self.id[node])
        return self.id[node]
    
    def isConnected(self,p,q):
        return self.root(p) == self.root(q)
    
    def union(self, p, q):
        proot = self.root(p)
        qroot = self.root(q)
        if self.size[proot] >= self.size[qroot] :
            self.id[qroot] = proot
            self.size[proot] = self.size[proot] + self.size[qroot]
        else:
            self.id[proot] = qroot
            self.size[qroot] = self.size[qroot] + self.size[proot]

runner = unionFind()
runner.union(4,5)
runner.union(3,4)
runner.union(1,2)
runner.union(4,1)
runner.union(7,9)
print(runner.isConnected(2,4))
print(runner.isConnected(3,5))