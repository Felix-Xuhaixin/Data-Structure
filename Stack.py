# LIFO principle: Last In, First Out (LIFO)

class Node:
    def __init__(self,value):
        self.value = value
        self.next = None


class Stack:
    def __init__(self):
        self.top = None
        self.size = 0 
    
    def push(self,value):
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node
        self.size += 1

        
    def __printStack__(self):
        item = []
        current_item = self.top
        while current_item is not None:
            item.append(current_item.value)
            current_item = current_item.next

        return print(item)
      
    def pop(self):
        print (self.top.value)
        self.top = self.top.next
        self.size -= 1 




if __name__ == "__main__":
    mystack = Stack()
    mystack.push(7)
    mystack.push(9)
    mystack.push(11)
    mystack.push(13)
    mystack.push(17)
    mystack.push(19)
    mystack.push(23)
    mystack.pop()
    mystack.__printStack__()

    