class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        
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
            

    def append(self,value):
        if self.head is None:
            self.head = Node(value)
        else:
             last = self.head
             while last.next != None:
                 last = last.next
             last.next = Node(value)    
    
    def prepend(self,value):
        if self.head is None:
            self.head = Node(value)
        else:
            first = Node(value)
            first.next = self.head
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
            last.next = new_node
             

    def  delete(self,value):
        if self.head.value == value:
            self.head = self.head.next
        else:
            last = self.head
            while last.next.value != value:
                last = last.next
                if last.next == None:
                    return print('value out of bounds')
            temp_node = last.next
            last.next = temp_node.next


    def get(self,index):
        pass

    def pop(self,index):
        pass        
         
            
        

if __name__ == "__main__":
    mylinkedlist = LinkedList()
    mylinkedlist.append(11)
    mylinkedlist.append(13)
    mylinkedlist.append(17)
    mylinkedlist.append(19)
    mylinkedlist.append(23)
    mylinkedlist.append(29)
    mylinkedlist.prepend(7)
    mylinkedlist.insert(18,4)
    mylinkedlist.append('Felix')
    mylinkedlist.len()
    mylinkedlist.contain(11)
    mylinkedlist.contain(25)
    mylinkedlist.delete(7)
    mylinkedlist.printList()



