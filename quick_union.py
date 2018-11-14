class unionFind(object):
    def __init__(self):
        self.id = [0,1,2,3,4,5,6,7,8,9]

    def root(self,node):
        while self.id[node]!= node:
            node = self.id[node]
        return node
    
    def isConnected(self,p,q):
        return self.root(p) == self.root(q)
    
    def union(self, p, q):
        proot = self.root(p)
        qroot = self.root(q)
        self.id[proot] = qroot

runner = unionFind()
runner.union(4,5)
runner.union(3,4)
runner.union(1,2)
runner.union(7,9)
print(runner.isConnected(7,1))
print(runner.isConnected(3,5))