class quickFind(object):
    
    def __init__(self):
        self.list = [0,1,2,3,4,5,6,7,8,9]

    def isConnected(self,node1,node2):
        return self.list[node1] == self.list[node2]
    
    def union(self,node1,node2):
        for i in range(len(self.list)):
            if self.list[i] == self.list[node1]:
                self.list[i] = self.list[node2]


runner = quickFind()
runner.union(4,5)
runner.union(3,4)
runner.union(1,2)
runner.union(7,9)
print(runner.isConnected(7,1))
print(runner.isConnected(3,5))
