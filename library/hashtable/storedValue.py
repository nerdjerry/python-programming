class storedValue(object):

    def __init__(self,key,value):
        self.key = key
        self.value = value
    
    def __str__(self):
        return "Key: {} , Value: {}".format(self.key,self.value)