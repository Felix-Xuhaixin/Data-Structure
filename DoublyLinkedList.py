class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
        self.previous = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        
    def printList(self):
        if self.head is None:
            print("[]")
        else:
            last = self.head

            return_string = f"[{last.value}"
            
            while last.next:
               last = last.next 
               return_string += f", {last.value}"
            return_string += "]"
            
            print(return_string)
            
# 0(1) constant time
    def append(self,value):
        if self.head is None:
            self.head = Node(value)
            self.tail = self.head
        else:
             last_node = Node(value)
             last_node.previous = self.tail
             self.tail.next = last_node
             self.tail = last_node
             
                
    
    def prepend(self,value):
        if self.head is None:    
            self.head = Node(value)
            self.tail = self.head
        else:
            first = Node(value)
            first.next = self.head
            self.head.privious = first
            self.head = first

    def len(self):
        n = 0
        last = self.head
        while last is not None:
            n += 1
            last = last.next
            
        print(n)            


    def contain(self,value):
        last = self.head
        while last is not None:
            if last.value == value:
              return print('True')
            last = last.next
        return print('False')      

    def insert(self,value,index): 
        if index == 0:
            self.append(value)
        else:
            last = self.head
            n = 0
            while n != (index - 1):
                last = last.next
                n += 1
            new_node = Node(value)
            new_node.next = last.next
            new_node.previous = last   
            last.next.previous = new_node
            last.next = new_node
             

    def  delete(self,value):
        if self.head.value == value:
            self.head = self.head.next
            self.head.previous = None
        else:
            last = self.head
            while last.next.value != value:
                last = last.next
                if last.next == None:
                    return print('value out of bounds')
            temp_node = last.next
            last.next = temp_node.next
            temp_node.next.previous = last


    def get(self,index):
        pass

    def pop(self,index):
        pass        
         
        
 
if __name__ == "__main__":
    ll = DoublyLinkedList()
    ll.append(11)
    ll.append(13)
    ll.insert(17,1)
    ll.insert(19,1)
    ll.insert(23,1)
    ll.insert(29,1)
    ll.insert(31,1)
    ll.insert(37,1)
    ll.insert(41,1)
    ll.insert(43,1)
    ll.delete(31)
    ll.prepend(31)

    ll.printList()