class HashMap:
    
    def __init__(self,capacity): 
        self.capacity = capacity # The capacity is the number of buckets
        self.size = 0 # size is the number of elements in the hashmap
        self.buckets = [[] for _ in range (capacity)] 

    def __len__(self):
        print(self.size)


    def __contains__(self,key):
        index = self._hash_function(key)
        bucket = self.buckets[index]
        
        for k, v in bucket:
            if  k == key:
                print(True)

        print (False)     


    def put(self,key,value):
        index = self._hash_function(key)
        bucket = self.buckets[index]

        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key,value)
                break
        else:
            bucket.append((key,value))  
            self.size += 1

    
    def get(self,key):
        index = self._hash_function(key)
        bucket = self.buckets[index]
        
        for k, v in bucket:
            if  k == key:
                print(v)
            else:
                print ('key not found')  

    def remove(self,key):
        index = self._hash_function(key)
        bucket = self.buckets[index]
        
        for i, (k, v) in enumerate(bucket):
            if k == key:
                del bucket[i]
                self.size -= 1
                break
        else:
            print("key not found")
                

    def keys(self):
        print([k for bucket in self.buckets for k, _ in bucket])

    def values(self):
        print([v for bucket in self.buckets for _, v in bucket])
        
    
    def items(self):
        print([(k,v) for bucket in self.buckets for (k,v) in bucket])

    def _hash_function(self, key):
        key_string = str(key)
        hash_result = 0
        
        for c in key_string:
            hash_result = (hash_result * 31 + ord(c)) % self.capacity
            
        return hash_result
    


if __name__ == "__main__":
    my_HashMap = HashMap(32)
    my_HashMap.put("Felix","Large")
    my_HashMap.put("Andrew","Long")
    my_HashMap.put("Ronald","Hard")
    my_HashMap.put("Jia","Smooth")
    my_HashMap.put("Liya","Voluptuous")
 
    print(my_HashMap.buckets)
    my_HashMap.get('Liya')
    my_HashMap.keys()
    my_HashMap.items()
    my_HashMap.remove('Andrew')
    my_HashMap.items()