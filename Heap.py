"""
left = index * 2 +1
right = index * 2 +2
parent = (index - 1) // 2 
"""

class MinHeap:
    
    def __init__(self):
        self.heap = []


    def __len__(self):
        return len(self.heap)
    
    def __repr__(self):
        return str(self.heap)
    
    def insert(self, key, value):
        self.heap.append((key,value))
        self._sift_up(len(self.heap)-1) # the last one index
    
    def peek_min(self):
        if not self.heap:
            raise IndexError('Empty heap')
        return self.heap[0]
    
    def extract_min(self):
        if not self.heap:
            raise IndexError('Empty heap')
        min_element = self.heap[0]
        last_element = self.heap[len(self.heap)-1]  
        
        if self.heap: # not the empty list
            self.heap[0] = last_element
            self._sift_down(0)

        return min_element           
        

    def heapify(self,elements):
        self.heap = list(elements)
        
        for i in reversed(range(self._parent(len(self.heap)-1)+1)):
            self._sift_down(i)

    def _parent(self,index):
        return (index - 1) // 2 if index != 0 else None

    def _left(self,index):
        left = index * 2 + 1
        return left if left < (len(self.heap)) else None
    
    def _right(self,index):
        right = index * 2 + 2
        return right if right < (len(self.heap)) else None
    
    def _sift_up(self, index): 
        # swim 
        parent_index = self._parent(index)
        
        while parent_index is not None and self.heap[index][0] < self.heap[parent_index][0]:
            self.heap[index],self.heap[parent_index] = self.heap[parent_index], self.heap[index]
            index = parent_index
            parent_index = self._parent(index) 

    def _sift_down(self,index):
        # sink
        while True:
            smallest = index
            
            left = self._left(index)
            right = self._right(index)

            # if self.heap[left][0] is not None and self.heap[index][0] > self.heap[left][0]:
            #     self.heap[index],self.heap[left] = self.heap[left], self.heap[index]
            #     index = left

            # elif self.heap[right][0] is not None and self.heap[index][0] > self.heap[right][0]:
            #     self.heap[index],self.heap[right] = self.heap[right], self.heap[index] 
            #     index = right
 
            # else:
            #     break
                
            if left is not None and self.heap[left][0] < self.heap[smallest][0]:
                smallest = left
            
            if right is not None and self.heap[right][0] < self.heap[smallest][0]:
                smallest = right

            if smallest == index:
                break

            self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
            index = smallest



if __name__ == "__main__":
    myHeap = MinHeap()
    myHeap.heapify([[10,'10'],[9,'9'],[8,'8'],[7,'7'],[6,'6'],[5,'5'],[4,'4'],[3,'3'],[2,'2'],[1,'1']])
    print(myHeap)   

    import heapq
    mylist =[10,9,8,7,6,5,4,3,2,1]
    heapq.heapify(mylist)
    print(mylist)