class hashtable(object):

    def __init__(self):
        self.table = [None] * 20

    def put(self,key,value):
        hashedKey = self.hash(key)
        if self.table[hashedKey] != None:
            print("Cant't insert collision occured")
        self.table[hashedKey] = value
    
    def get(self,key):
        return self.table[self.hash(key)]

    def hash(self,key):
        return len(key) % 20

ht = hashtable()
ht.put("Prateek",34)
ht.put("Aditi",23)
ht.put("Somya",21)
print(ht.get("Prateek"))