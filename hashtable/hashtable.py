from storedValue import storedValue

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
        self.table[hashedKey] = storedValue(key,value)
    
    def get(self,key):
        hashedKey = self.hash(key)
        value = None
        if self.occupied(hashedKey) and self.table[hashedKey].key == key:
            value = self.table[hashedKey].value
            self.table[hashedKey] = None
        else:
            initialKey = hashedKey
            hashedKey = (hashedKey + 1 ) % self.capacity
            while self.occupied(hashedKey) and self.table[hashedKey].key != key and initialKey != hashedKey:
                hashedKey = (hashedKey + 1) % self.capacity
            if self.occupied(hashedKey) and self.table[hashedKey].key == key:
                value = self.table[hashedKey].value
                self.table[hashedKey] = None
        initialKey = hashedKey
        hashedKey = (hashedKey + 1) % self.capacity
        while self.occupied(hashedKey) and initialKey != hashedKey:
            key = self.table[hashedKey].key
            value =  self.table[hashedKey].value
            self.table[hashedKey] = None
            self.put(key,value)
            hashedKey =(hashedKey + 1) % self.capacity
        return value
        

    def hash(self,key):
        return len(key) % self.capacity
    
    def occupied(self, key):
        return self.table[key] != None

ht = hashtable()
ht.put("Prateek",34)
ht.put("Aditi",23)
ht.put("Aditi2",12)
ht.put("Aditi23",13)
ht.put("Somya",21)
ht.put("Sonal",123)
ht.put("Aditi",122)
print(ht.get("Aditi"))
print(ht.get("Somya"))
print("Helllo")