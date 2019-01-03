class hashtable(object):

    def __init__(self):
        self.capacity = 20
        self.table = [None] * self.capacity

    def put(self,key,value):
        hashedKey = self.hash(key)
        if self.occupied(hashedKey):
            initialKey = hashedKey
            hashedKey = (hashedKey + 1) % self.capacity
            while self.occupied(hashedKey) and hashedKey != initialKey:
                hashedKey = (hashedKey + 1) % self.capacity
        if self.occupied(hashedKey):
            print("Can't insert element as there is no place")
            #you can resize table here
        self.table[hashedKey] = value
    
    def get(self,key):
        return self.table[self.hash(key)]

    def hash(self,key):
        return len(key) % self.capacity
    
    def occupied(self, key):
        return self.table[key] != None

ht = hashtable()
ht.put("Prateek",34)
ht.put("Aditi",23)
ht.put("Somya",21)
print(ht.get("Prateek"))